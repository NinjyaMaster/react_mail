import React, { useState, useContext, useEffect } from "react";
import Button from "../components/Button.js";
import useFetch from "../utls/useFetch.js";
//import { TokenContext } from "../../App.js";
import { useCookies } from "react-cookie";

//<Button>Login</Button>
export default function Login(props) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [username, setUsername] = useState("");
  const [isLoginFail, setIsLoginFail] = useState(false);
  const [isLoginView, setIsLoginView] = useState(true);

  //const { token, setToken } = useContext(TokenContext);
  const [token, setToken] = useCookies(["mail-token"]);
  const { post } = useFetch("http://127.0.0.1:8000/");

  useEffect(() => {
    //console.log(token);
    //console.log("I set Token");
    // token from contexxt
    //if (token) window.location.href = "/inbox";
    if (token["mail-token"] && token["mail-token"] !== undefined) {
      console.log(`*****redirect to ${token}`);
      window.location.href = "/mail/inbox/";
    }
  }, [token]);

  const handleLoginClick = () => {
    post("udemy_auth/udemy_token/", { email, password })
      .then((data) => {
        console.log(data);
        if (data.token) {
          //setToken(data.token); // this is for context
          setToken("mail-token", data.token, { path: "/" });
          setIsLoginFail(false);
        } else {
          setIsLoginFail(true);
        }
      })
      .catch((error) => console.log(error));
  };

  const handleRegisterClick = () => {
    post("udemy_auth/udemy_register/", { email, password, username })
      .then((data) => {
        if (data.token) {
          setToken("mail-token", data.token, { path: "/" });
          //console.log(`*****setToken from handle Register ${token}`);
          setIsLoginFail(false);
        } else {
          setIsLoginFail(true);
          //console.log(data);
          handleLoginClick();
        }
      })
      .catch((error) => console.log(error));
  };

  return (
    <div className="main">
      {isLoginView ? (
        <h2 className="userName">Login</h2>
      ) : (
        <h2 className="userName">Register</h2>
      )}
      {isLoginFail && isLoginView ? <h2>Login Failed</h2> : ""}
      <input
        id="email"
        type="text"
        placeholder="email"
        value={email}
        onChange={(evt) => setEmail(evt.target.value)}
        className="form-textinput"
      />
      <br />
      <input
        id="password"
        type="password"
        placeholder="password"
        value={password}
        onChange={(evt) => setPassword(evt.target.value)}
        className="form-textinput"
      />
      <br />
      {isLoginView ? (
        <></>
      ) : (
        <input
          id="username"
          type="username"
          placeholder="username"
          value={username}
          onChange={(evt) => setUsername(evt.target.value)}
          className="form-textinput"
        />
      )}
      {isLoginView ? (
        <Button onClick={handleLoginClick} className="buttonInactive">
          Login
        </Button>
      ) : (
        <Button onClick={handleRegisterClick} className="buttonInactive">
          Register
        </Button>
      )}
      {isLoginView ? (
        <p onClick={() => setIsLoginView(false)} className="loginText">
          You don't have an account? Register here!
        </p>
      ) : (
        <p onClick={() => setIsLoginView(true)} className="loginText">
          You already have an account? Login here
        </p>
      )}
    </div>
  );
}
