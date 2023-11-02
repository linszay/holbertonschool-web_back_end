// server file
import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import morgan from 'morgan';
import routes from './routes';

const app = express();

app.use(bodyParser.json());
app.use(cors());
app.use(morgan('combined'));
app.use('/', routes);

app.locals.database = process.argv[2];

app.listen(1245, () => {
  console.log(`Server is running on port 1245`);
});

export default app;
