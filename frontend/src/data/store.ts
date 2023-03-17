import { configureStore, ThunkAction, Action } from "@reduxjs/toolkit";
import { setupListeners } from "@reduxjs/toolkit/query";
import accountReducer from "./account/account.slice";
import orderReducer from "./order/order.slice";
import productReducer from "./product/product.slice";
import shoppingCartReducer from "./shopping_cart/shoppingCart.slice";

export const store = configureStore({
  reducer:{
    account: accountReducer,
    order: orderReducer,
    product: productReducer,
    shopping: shoppingCartReducer
  }
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<ReturnType, RootState, unknown, Action<string>>;

setupListeners(store.dispatch);
