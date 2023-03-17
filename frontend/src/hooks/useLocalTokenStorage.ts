import React, { useState, useEffect } from "react";
import { getLocalToken, saveLocalToken, removeLocalToken } from "../utils/tokenUtils";

function useLocalTokenStorage() {
  //use user selector to get the token
  //check if the user token is expired
  //if expired redirect to login
  //if not expired redirect to user dashboard page

  const [token, setToken] = useState('');

  useEffect(() => {

  }, []);

  return { };
}
