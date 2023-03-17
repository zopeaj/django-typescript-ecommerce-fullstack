import { TypedUseSelectHook, useDispatch, useSelector } from "redux/react";
import type { RootState, AppDispatch } from "./store";

export const useAppDispatch = () => useDispatch<AppDispatch>()
export const useAppSelector: TypedUseSelectHook<RootState> = useSelector;
