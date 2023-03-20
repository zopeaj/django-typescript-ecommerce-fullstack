import { createAsyncThunk } from "@reduxjs/toolkit";
import { removeOrders } from "./api/orderApi";

export const deleteOrders = createAsyncThunk("order/deleteOrders", async (id: number) => {

});
