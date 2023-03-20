import { createEntityAdapter } from "@reduxjs/toolkit";
import { Product } from "../product/product.state";

export interface ShoppingCart {
  shopping_id: number,
  account_id: number,
  products: Product[],
  selected: boolean,
  created: string,
  updated: string,
}

export interface ShoppinCartState {
  shopping_cart: ShoppingCart,
  isLoading: boolean,
  errors: any,
  success: any,
}

export const initialState: ShoppinCartState = createEntityAdapter.getInitialState({

})
