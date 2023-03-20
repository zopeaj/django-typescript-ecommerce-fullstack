import React from 'react';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { createTheme } from "@mui/material/styles";

function App(){
  return (
     <BrowserRouter>
       <Routes>
         <Route path="/" element={<Start />}>
           <Route index element={<Main />} />
           <Route path='about' element={<About />}/>

           <Route path="account" element={<Dashboard/>}>
             <Route index element={<AccountProfile />} />
             <Route path=":accountId:/profile-edit" element={<AccountProfileEdit />} />
             <Route path=":accountId:/profiled-edit-password" element={<AccountProfileEditPassword />} />
           </Route>

           <Route path="products" element={<SharedProductLayout />}>
             <Route index element={<Products />} />
             <Route path=":productId" element={<SingleProduct/>} />
             <Route path=":productId/details" element={<ProductDetails />} />
             <Route path=":productId/update" element={<ProdutUpdates />} />
           </Route>

           <Route path='login' element={<Login />} />
           <Route path='register' element={<Register />} />
           <Route path="*" element={<ErrorPage />} />
         </Route>
       </Routes>
     </BrowserRouter>
  );
};


export default App;
