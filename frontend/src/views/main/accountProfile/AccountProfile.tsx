import React, { useState } from "react";
import { useAppDispatch } from "../../../app/hooks";
import {
  username
} from "../../../data/account/account.selector";
import { Link } from "react-router-dom";
import { Button } from "@mui/material";

const AccountProfile: React.FC<> = (): any => {
  return (
     <div>
       <div className={styles.container}>
         <div className={styles.header}>
           <div>App Logo</div>
           <div>
             <h3>Welcome {username} !</h3>
           </div>
           <div>
             <Button variant="contained" to="/update-profile" component={Link}>Update</Button>
           </div>
         </div>
       </div>
       <div className={styles.mainContainer}>
         <div>
           <h3>Hello World</h3>
         </div>
       </div>
     </div>
  );
}
export default AccountProfile;
