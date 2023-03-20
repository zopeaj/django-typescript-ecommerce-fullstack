import { useAppSelector } from "../../app/hooks";
import { RootState } from "../../app/store";

export const getProducts = (state: RootState) => state.product.products;
