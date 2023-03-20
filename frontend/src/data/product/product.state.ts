import { createEntityManager } from "@reduxjs/toolkit";

export interface Product {
  name: string;
  price: number;
  category: string;
  image: any,
  created: string;
  updated: string;
  quantity: number;
  total_price: number;
  vat: number;
}

export interface ProductState {
  products: Product[],
  isLoading: boolean,
  errors: any,
  success: any,
}

export const initialState: ProductState = createEntityManager.getInitialState({
  products: null,
  isLoading: false,
  errors: null,
  success: null,
});



