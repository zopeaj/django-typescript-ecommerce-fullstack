const env = process.env.TYPESCRIPTREACT_APP_ENV;

let envApiUrl = '';

if (env === 'production') {
  envApiUrl = `https://${process.env.TYPESCRIPTREACT_APP_DOMAIN_PROD}`;
} else if (env === 'staging') {
  envApiUrl = `https://${process.env.TYPESCRIPTREACT_APP_DOMAIN_STAG}`;
} else {
  envApiUrl = `http://${process.env.TYPESCRIPTREACT_APP_DOMAIN_DEV}`;
}

export const API_URL = envApiUrl;
export const appName = process.env.TYPESCRIPTREACT_APP_NAME;

