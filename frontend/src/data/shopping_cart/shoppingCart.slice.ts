import { createSlice } from "@redux/toolkit";
import { initialState } from "./shoppingCart.state";

export const shoppingCartSlice = createSlice({
  name: 'shoppingCart',
  initialState,
  reducers: {

  }
})

export default shoppingCartSlice.reducer;
