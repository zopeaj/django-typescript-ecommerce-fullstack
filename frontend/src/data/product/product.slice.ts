import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { initialState } from "./product.state";


export const productSlice = createSlice({
  name: 'product',
  initialState,
  reducers: {
    products: (state: any, action: PayloadAction<any>) => {
      state = { ...state, products: action.payload.products };
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
  },
  extraReducers: (builder: any) => {
    builder
      .addCase(, (state: any, action: any) => {

      })
  }
})

export default productSlice.reducer;
export const { products, isLoading, errors, success } = productSlice.actions
