import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import authRoutes from './routes/auth.routes';
import jobsRoutes from './routes/jobs.routes';
import statsRoutes from './routes/stats.routes';
import { errorHandler } from './middleware/errorHandler';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 4000;

app.use(cors({ origin: process.env.CLIENT_URL }));
app.use(express.json());

app.use('/api/auth', authRoutes);
app.use('/api/jobs', jobsRoutes);
app.use('/api/stats', statsRoutes);

app.use(erroeHandler);

app.listen(PORT, () => {
  console.log('Server running on port ${PORT}');
});
