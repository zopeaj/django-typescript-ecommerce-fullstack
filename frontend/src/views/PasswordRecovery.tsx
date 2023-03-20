import React, { useState, Fragment } from "react";
import {
  Typography,
  Meny,
  Grid,
  Card,
  CardContent,
  List,
  ListItemText
} from "@mui/material";


interface PasswordRecovery { }

const PasswordRecovery: React.FC<PasswordRecovery> = (): any => {

  const handlePasswordRecovery = (e: React.ChangeEvent<any>) => {

  }

  return (
     <Fragment>
       <div>
         <form onSubmit={handlePasswordRecovery}>

         </form>
       </div>
     </Fragment>
  );
}

export default PasswordRecovery;
