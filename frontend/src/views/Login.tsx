import React, { useState, useHistory } from "react";
import { useAppDispatch } from "../data/hooks";
import { actionLogin } from "../data/user/user.actions"
import { RootState } from "../data/store";

interface State { }

const Login:React.FC = () => {
  const history = useHistory();
  const [password, setPassword] = useState('');
  const dispatch = useAppDispatch();

  const handleLogin = (event: React.Event) => {

    var formData = new FormData();
    dispatch(actionLogin(RootState, formData));
  };

  return (
   <div>
     <form onSubmit={handleLogin}>

     </form>
   </div>
  );
}
