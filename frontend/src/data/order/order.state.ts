import { createEntityAdapter } from "@reduxjs/toolkit";
import { ShoppingCart } from "../shopping_cart/shoppingCart.state";


export interface Order {
  order_id: number;
  account_id: number;
  shopping_carts: ShoppingCart;
  created: string;
  update: string;
}

export interface OrderState {
  orders: Order[],
  isLoading: boolean,
  errors: any,
  success: any,
}

export const initialState: OrderState = createEntityAdapter.getInitialState({
  orders: null,
  isLoading: false,
  errors: null,
  success: null,
})
