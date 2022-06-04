import React, { useEffect, useState } from "react";
import { Link, NavLink } from "react-router-dom";
import { useCookies } from "react-cookie";
import useAuthFetch from "../utls/useAuthFetch.js";
import Button from "./Button";

export default function Navbar(props) {
  const [token] = useCookies(["mail-token"]);
  const [user, setUser] = useState([]);

  const { toggleDarkTheme } = props;

  const { get, loading } = useAuthFetch(
    "http://127.0.0.1:8000/",
    token["mail-token"]
  );

  useEffect(() => {
    let userInfoPath = "udemy_auth/udemy_me/";

    get(userInfoPath)
      .then((data) => {
        console.log(data);
        setUser(data);
      })
      .catch((error) => {
        console.log("Could not load user info", error);
      });
  }, []);

  return (
    <header className="header">
      <div className="header-inner">
        <div className="userName">
          {user.email} - {user.username}
          <Button onClick={() => toggleDarkTheme()}>toggleDarkTheme</Button>
        </div>
        <ul className="nav">
          <li>
            <NavLink
              to="/mail/inbox/"
              className={({ isActive }) =>
                isActive ? "buttonActive" : "buttonInactive"
              }
            >
              Inbox
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/mail/compose/"
              className={({ isActive }) =>
                isActive ? "buttonActive" : "buttonInactive"
              }
            >
              Compose
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/mail/sent/"
              className={({ isActive }) =>
                isActive ? "buttonActive" : "buttonInactive"
              }
            >
              Sent
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/mail/archived/"
              className={({ isActive }) =>
                isActive ? "buttonActive" : "buttonInactive"
              }
            >
              Archived
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/logout/"
              className={({ isActive }) =>
                isActive ? "buttonActive" : "buttonInactive"
              }
            >
              Logout
            </NavLink>
          </li>
        </ul>
      </div>
    </header>
  );
}

//activeClassName="active"
