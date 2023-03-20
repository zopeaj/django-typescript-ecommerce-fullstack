import { API_URL } from "../../../env";
import { isLoading, user, errors, success, isAuthenticated, authenticationError } from "../account.slice";
import { selectUserId, selectUserToken } from "../account.selector";
import { AppThunk } from "../../../app/store";
import { selectUser } from "../account.selector";


const checkStatus =( response: any) => {
  if(response.ok) {
    return response;
  }
  const error = new Error(response.statusText);
  error.response = response;
  return Promise.reject(error);
}

export const registerAccount = (data: any): AppThunk => (dispatch: any, getState: any) =>  {
  dispatch(isLoading(true))
  return fetch(API_URL + "/api/api/auth", {
    method: 'POST',
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data)
      }).then(checkStatus)
        .then((res) => {
          if(res.status < 500) {
            res.json()
            dispatch(success(res));
          }else {
            dispatch(errors(res));
          }
        }).catch((err) => {
          err.response.json().then((res: any) => {
            dispatch(errors(res));
          });
      }).finally(() => {
        dispatch(isLoading(false));
    })
}

export const loadAccount = (): AppThunk => (dispatch: any, getState: any) => {
  const token = selectUserToken(getState())
  const accountId = selectUserId(getState());
  let headers: any = {
    "Content-Type": "application/json",
  }
  if(token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  return fetch(API_URL + "/api/account" + accountId, {
    method: "GET",
    headers
  }).then(checkStatus)
      .then(res => {
        if(res.status < 500) {
          res.json()
        } else {
          //dispatch(status(res));
        }
      })
      .then(data => {
        dispatch(user(data));
      })
      .catch(err => {
        err.response.json().then((res: any) => {
          dispatch(errors(res));
        })
      }).finally(() => isLoading(false));
}

export const updateAccount = (id: number, data: any): AppThunk => (dispatch: any, getState: any) => {
  dispatch(isLoading(true));
  const token = selectUserToken(getState());
  const accountId = selectUserId(getState());
  const user = selectUser(getState());
  let headers: any = {
    "Content-Type": "application/json",
  }
  if(token) {
    headers['Authorization'] = `Bearer ${token}`;
  }
  let body = JSON.stringify(data);
  return fetch(API_URL + "/api/account" + accountId, {
    method: "PUT",
    headers,
    body: JSON.stringify(data)
  }).then(checkStatus)
      .then(res => {
        if(res.status < 500) {
          res.json()
        }else{
          // dispatch(status(res))
        }
      })
      .then(data => {
        dispatch(user(data));
      })
      .catch(err => {
        err.response.json().then((res: any) => {
          dispatch(errors(res));
        })
      })
    .finally(() => isLoading(false));
}

export const deleteAccount = (): AppThunk => (dispatch: any, getState: any) => {
  dispatch(isLoading(true))
  const accountId = selectUserId(getState());
  const token = selectUserToken(getState());

  let headers: any = {
    "Content-Type": "application/json"
  };

  if(token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  return fetch(API_URL + "/api/account" + accountId, {
    method: "DELETE",
    headers,
  }).then(checkStatus)
    .then(() => {

    }).catch((err: any) => {
      err.response.json().then((res: any) => {
        console.log(res);
        dispatch(errors(res));
      });
    }).finally(() => dispatch(isLoading(false)));
}

export const loginAccount = (data: any) => {
  let headers = {
      "Content-Type": "application/json"
  };
  return fetch(API_URL + "/api/auth/login", {
    method: "POST",
    headers,
    body: JSON.stringify(data)
  }).then(checkStatus)
}

export const logout = (data: any):AppThunk => (dispatch: any, getState: any) => {
  dispatch(isLoading(false));
  let token: string = selectUserToken(getState());
  let headers: any = {
    'Content-Type': 'application/json'
  };

  if(token) {
    headers['Authorization'] = `Bearer ${token}`;
  }
  return fetch(API_URL + '/api/auth/logout',{
    method: "POST",
    headers,
    body: JSON.stringify(data)
  }).then(checkStatus)
      .then(res => res.json())
        .then(data => {
          dispatch(success(data));
        })
        .catch(err => {
           err.response.json().then((res: any) => {
               dispatch(errors(res));
           });
        }).finally(() => dispatch(isLoading(false)));
}
