// import { StrictMode } from 'react'
// import { createRoot } from 'react-dom/client'
// import './index.css'
// import App from './App.tsx'

// createRoot(document.getElementById('root')!).render(
//   <StrictMode>
//     <App />
//   </StrictMode>,
// )

// import React from 'react';
import { createRoot } from 'react-dom/client';
import { Auth0Provider } from '@auth0/auth0-react';
import App from './App';


const root = createRoot(document.getElementById('root')!);

root.render(
<Auth0Provider
    domain="dev-4b7mjenwz3wlwl0k.us.auth0.com"
    clientId="ZmqN7mjfjbzsorUdctjam15BkaHFtGh2"
    authorizationParams={{
      redirect_uri: window.location.origin
    }}
  >
    <App />
  </Auth0Provider>,
);
