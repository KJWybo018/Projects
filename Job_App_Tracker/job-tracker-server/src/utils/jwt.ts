import jwt from 'jsonwebtoken';
import { config } from '../config/env';
import { AuthPayload } from '../types';

export const signToken = (payload: AuthPayload): string =>
  jwt.sign(payload, config.jwtSecret, { expiresIn: config.jwtExpiresIn } as jwt.SignOptions);

export const verifyToken = (token: string): AuthPayload =>
  jwt.verify(token, config.jwtSecret) as AuthPayload;
