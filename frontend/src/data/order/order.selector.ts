import { useAppSelector } from "../../app/hooks";
import { RootState } from "../../app/store";
import { Order } from "./order.state";

export const getOrders = (state: RootState) => state.order.orders
