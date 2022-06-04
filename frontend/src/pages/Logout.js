import React, { useEffect } from "react";
import { useCookies } from "react-cookie";

export default function Logout() {
  const [token, setToken, removeToken] = useCookies(["mail-token"]);

  useEffect(() => {
    removeToken("mail-token", { path: "/" });
    console.log("I removed your token");
    console.log(`**********************${token["mail-token"]}`);
    console.log("I removed your token");
  }, []);

  useEffect(() => {
    console.log(`**********************${token["mail-token"]}`);
    if (!token["mail-token"] || token["mail-token"] == undefined) {
      window.location.href = "/";
    }
  }, [token]);

  return <di>Youa re logged out!</di>;
}
