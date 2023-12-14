import { useState } from "react";
import * as Yup from "yup";
import { useFormik } from "formik";
import { useDispatch } from "react-redux";
import authSlice from "../store/slices/auth";
import axios from "axios";
import { useHistory } from "react-router";

function Signup() {
  const [loading, setLoading] = useState(false);
  const dispatch = useDispatch();
  const history = useHistory();

  const handleLogin = (email: string, password: string, username: string) => {
    axios
      .post(`${process.env.REACT_APP_API_URL}auth/register/`, { email, password, username })
      .then((res) => {
        dispatch(
          authSlice.actions.setAuthTokens({
            token: res.data.access,
            refreshToken: res.data.refresh,
          })
        );
        dispatch(authSlice.actions.setAccount(res.data.user));
        setLoading(false);
        history.push("/", {
          userId: res.data.id
        });
      })
  };

  const formik = useFormik({
    initialValues: {
      email: "",
      password: "",
      username: "",
    },
    onSubmit: (values) => {
      setLoading(true);
      handleLogin(values.email, values.password, values.username);
    },
    validationSchema: Yup.object({
      email: Yup.string().trim().required("Please, enter your email"),
      password: Yup.string().trim().required("Please, enter your password").min(8, 'Must be at least 8 digits'),
      username: Yup.string().trim().required("Please, enter your username"),
    }),
  });
  return (
    <div className="h-screen flex bg-gray-bg1">
      <div className="w-full max-w-md m-auto bg-white rounded-lg border border-primaryBorder shadow-default py-10 px-16">
        <h1 className="text-2xl font-medium text-primary mt-4 mb-12 text-center">
          Sign up to your account 🆕
        </h1>
        <form onSubmit={formik.handleSubmit}>
          <div className="space-y-4">
            <input
              className="border-b border-gray-300 w-full px-2 h-8 rounded focus:border-blue-500"
              id="email"
              type="email"
              placeholder="Email"
              name="email"
              value={formik.values.email}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
            />
            {formik.errors.email ? <div>{formik.errors.email} </div> : null}
            <input
              className="border-b border-gray-300 w-full px-2 h-8 rounded focus:border-blue-500"
              id="username"
              type="text"
              placeholder="Username"
              name="username"
              value={formik.values.username}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
            />
            {formik.errors.username ? <div>{formik.errors.username} </div> : null}
            <input
              className="border-b border-gray-300 w-full px-2 h-8 rounded focus:border-blue-500"
              id="password"
              type="password"
              placeholder="Password"
              name="password"
              value={formik.values.password}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
            />
            {formik.errors.password ? (
              <div>{formik.errors.password} </div>
            ) : null}
          </div>
          <div className="flex justify-center items-center mt-6">
            <button
              type="submit"
              disabled={loading}
              className="rounded border-gray-300 p-2 w-32 bg-blue-700 text-white"
            >
              Sign up
            </button>
          </div>
          <a href="/login" className="text-blue-400">I'm have an account</a>
        </form>
      </div>
    </div>
  );
}

export default Signup;
