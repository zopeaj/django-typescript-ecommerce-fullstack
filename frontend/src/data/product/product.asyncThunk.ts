import { createAsyncThunk } from "@reduxjs/toolkit";
import { deleteProduct } from "./api/productApi";

export const removeProduct = createAsyncThunk("product/removeProduct", async (id: number) => {

});
