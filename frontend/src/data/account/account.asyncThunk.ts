import { createAsyncThunk } from "@reduxjs/toolkit";
import { loginAccount } from "./api/accountApi";

export const login = createAsyncThunk("account/login", async (data: any) => {
  const response = await loginAccount(data);
  response.then((res: any) => {
    if(res.status === 200) {
      return res.status
    }
  }).then((data: any) => {
    if(data) {
      return data.json();
    }
  }).catch((err: any) => {
    return err;
  })
});
