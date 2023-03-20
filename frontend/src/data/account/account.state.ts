import { createEntityAdapter } from "@reduxjs/toolkit"
import { Order } from "../order/order.state";

interface User {
  username: string,
  first_name: string;
  last_name: string;
  email: string;
}

interface Account {
  user: User,
  age: number,
  avatar: any,
  active: boolean,
  userId: number;
}


export interface UserState {
 user: Account,
 isLoading: boolean,
 errors: any,
 success: any,
 token: string,
 isAuthenticated: boolean,
 authenticationError: any,
};


export const initialState: UserState = createEntityAdapter.getInitialState({
  user: null,
  isLoading: false,
  errors: { },
  success: { },
  token: null
});


