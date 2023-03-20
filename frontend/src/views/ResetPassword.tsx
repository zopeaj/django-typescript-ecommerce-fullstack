import React, { useState, Fragment } from 'react';
import {
  AppBar,
  ToolBar,
  Button,
  Card,
  Grid,
  List,
  ListItemText
} from "@mui/material";


interface ResetPasswordProps { }

const ResetPassword: React.FC<ResetPasswordProps> = () => {
  return (
    <Fragment>
      <div>
         <AppBar class="reset-password-app-bar">
           <ToolBar class="reset-password-tool-bar">
             <div>
               App Logo
             </div>
           </ToolBar>
         </AppBar>
      </div>
      <div>

      </div>
    </Fragment>
  );
}

export default ResetPassword;
