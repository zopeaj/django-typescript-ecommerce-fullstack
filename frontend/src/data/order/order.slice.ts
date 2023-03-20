import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { initialState } from "./order.state";

export const orderSlice = createSlice({
  name: 'order',
  reducers: {
    orders: (state: any, action: PayloadAction<any>) => {
      state = { ...state, orders: action.payload.orders };
    },
    isLoading: (state: any, action: PayloadAction<any>) => {
      state = { ...state, isLoading: action.payload.isLoading };
    },
    errors: (state: any, action: PayloadAction<any>) => {
      state = { ...state, errors: action.payload.errors };
    },
    success: (state: any, action: PayloadAction<any>) => {
      state = { ...state, success: action.payload.success };
    }
  }
});

export default orderSlice.reducer;
export const { orders, isLoading, errors, success } = orderSlice.actions;
