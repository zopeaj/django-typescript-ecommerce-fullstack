import { useAppSelector } from "../../app/hooks";
import { RootState } from "../../app/store";

export const selectUser = (state: RootState) => state.account.user;
export const selectUserId = (state: RootState) => state.account.user.userId;
export const selectUserToken = (state: RootState) => state.account.user.token;
export const getUser = useAppSelector(selectUser);
export const selectUsername = (state: RootState) => state.account.user.username;
export const username = useAppSelector(selectUsername);
