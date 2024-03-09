import express from 'express';
import { promisify } from 'util';
import { createClient } from 'redis';

const app = express();
const redisclient = createClient();
const PORT = 1245;

app.use(express.json())

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5
  },
];


function getItemById(id) {
  let product = listProducts.find(product => product.itemId === id);

  if (product) return product;
}

async function reserveStockById(itemId, stock) {
  const setAsync = promisify(redisclient.SET).bind(redisclient);
  
  try {
    const response = await setAsync(`item.${itemId}`, stock);
    return response;
  } catch (err) {
    return err;
  }
}

async function getCurrentReservedStockById(itemId) {
  const getAsync = promisify(redisclient.GET).bind(redisclient);

  try {
    const response = await getAsync(`item.${itemId}`);
    return response;
  } catch (err) {
    return err;
  }
}

app.get('/list_products', (req, res) => {
  res.json(listProducts)
})

app.get('/list_products/:itemId(\\d+)', (req, res) => {
  const id = req.params.itemId;

  const product = getItemById(Number(id));

  if (product) {
    getCurrentReservedStockById(id).then(stock => {
      const reservedStock = Number(stock || 0)
      product.currentQuantity = product.initialAvailableQuantity - reservedStock;
      res.json(product)
    });
  } else {
    res.json({ status: 'Product not found' })
  }
})


app.get('/reserve_product/:itemId(\\d+)', (req, res) => {
  const id = req.params.itemId;

  const product = getItemById(Number(id));

  if (product) {
    getCurrentReservedStockById(id).then(stock => {
      const reservedStock = Number(stock || 0)
      if (reservedStock < Number(product.initialAvailableQuantity)) {
        reserveStockById(id, reservedStock + 1).then(() => {
          res.json({ status: 'Reservation confirmed', id });
        })
      } else {
        res.json({ status: 'Not enough stock available', id });
        return;
      }
    });
  } else {
    res.json({ status: 'Product not found' })
  }
})


app.listen(PORT)