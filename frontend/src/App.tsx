import React from 'react';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { createTheme } from "@mui/material/styles";
import { routes as appRoutes } from "./router/routes";
import Layout from "./components/Layout";
import { theme } from "./styles/themes";

function App(){
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Layout>
          <Routes>
            {appRoutes.map((route) => (
              <Route
                key={route.key}
                path={route.path}
                element={<route.component />}
              />
            ))}
          </Routes>
        </Layout>
      </Router>
    </ThemeProvider>
  );
};


export default App;
