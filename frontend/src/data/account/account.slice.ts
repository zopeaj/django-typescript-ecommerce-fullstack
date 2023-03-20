import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { initialState, UserState } from "./account.state"
import { login } from "./account.asyncThunk";

export const accountSlice = createSlice({
  name: 'account',
  initialState,
  reducers: {
    isLoading: (state: any, action: PayloadAction<any>) => {
      state = { ...state, isLoading: action.payload.isLoading };
    },
    user: (state: any, action: PayloadAction<any>) => {
      state = { ...state, user: action.payload.user };
    },
    errors: (state: any, action: PayloadAction<any>) => {
      state = { ...state, errors: action.payload.errors };
    },
    success: (state: any, action: PayloadAction<any>) => {
      state = { ...state, success: action.payload.success };
    },
    isAuthenticated: (state: any, action: PayloadAction<any>) => {
      state = { ...state, isAuthenticated: action.payload.isAuthenticated };
    },
    authenticationError: (state: any, action: PayloadAction<any>) => {
      state = { ...state, authenticationError: action.payload.authenticationError };
    }
  },
  extraReducers: (builder: any) => {
    builder
      .addCase(login.pending, (state: any) => {
        state.isLoading = true;
      })
      .addCase(login.fulfilled, (state: any, action: any) => {
        state.isLoading = false,
        state = { ...state, success: action.payload };
      })
      .addCase(login.rejected, (state: any, action: any) => {
        state = { ...state, errors: action.payload };
      })
  }
})

export default accountSlice.reducer;
export const { isLoading, user, errors, success, isAuthenticated, authenticationError } = accountSlice.actions
