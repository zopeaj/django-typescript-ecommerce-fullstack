import React, { useState, useEffect, Fragment } from "react";
import {
  Grid,
  Typography,
  AppBar,
  ToolBar,
  Button,
  Card,
  CardContent
} from "@mui/material";

interface Props {}

const Main: React.FC<Props> = (): any => {
  return (
    <Fragment>
      <div>
        <AppBar class="main-app-bar">
          <ToolBar class="main-tool-bar">
            <div class="app-logo">
              App Logo
            </div>
          </ToolBar>
        </AppBar>
      </div>
      <div>
        <Grid container>
          Hello Main
        </Grid>
      </div>
    </Fragment>
  );
}

export default Main;
