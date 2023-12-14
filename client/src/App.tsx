import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { Login, Work, Signup } from "./pages";
import store, { persistor } from "./store";
import { PersistGate } from "redux-persist/integration/react";
import { Provider } from "react-redux";
import ProtectedRoute from "./routes/ProtectedRoute";

export default function App() {
  return (
    <Provider store={store}>
      <PersistGate persistor={persistor} loading={null}>
        <Router>
          <div>
            <Switch>
              <Route exact path="/login" component={Login} />
              <Route exact path="/signup" component={Signup} />
              <ProtectedRoute exact path="/" component={Work} />
            </Switch>
          </div>
        </Router>
      </PersistGate>
    </Provider>
  );
}
