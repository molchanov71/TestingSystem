import * as React from 'react';
import * as ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import App from './App.js';
import './index.css';

const paths = [
    {
        path: '/',
        element: <App/>,
    },
]
const router = createBrowserRouter(paths);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<React.StrictMode>
    <RouterProvider router={router}/>
</React.StrictMode>
);
