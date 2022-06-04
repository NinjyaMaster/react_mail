import React, { useEffect, useState } from "react";
import { Route, Routes } from "react-router-dom";
import Compose from "./Compose.js";
import Mails from "./Mails.js";
import MailDetail from "./MailDetail.js";
import Navbar from "../components/Navbar.js";

export default function MailIndex() {
  const [isDarkTheme, setIsDarkTheme] = useState(false);

  useEffect(() => {
    if (isDarkTheme) {
      document.body.classList.add("dark");
    } else {
      document.body.classList.remove("dark");
    }
  }, [isDarkTheme]);

  // Set the theme based on the user's Operating System preferences.
  useEffect(() => {
    const prefersDark = window.matchMedia(
      "(prefers-color-scheme: dark)"
    ).matches;
    if (prefersDark) {
      //setIsDarkTheme(true);
    }

    //let darkTheme = localStorage.getItem("isDarkTheme");
    //setIsDarkTheme(darkTheme === "true");
  }, []);

  function handleThemeClick() {
    setIsDarkTheme(!isDarkTheme);
    //localStorage.setItem("isDarkTheme", true);
    //console.log(`****** set ${localStorage.getItem("isDarkTheme")}`);
  }

  return (
    <>
      <Navbar toggleDarkTheme={handleThemeClick} />
      <main className="main">
        <Routes>
          <Route path="inbox/" element={<Mails type="inbox" />} />
          <Route path="inbox/:id/" element={<MailDetail />} />
          <Route path="sent/" element={<Mails type="sent" />} />
          <Route path="sent/:id/" element={<MailDetail />} />
          <Route path="archived/" element={<Mails type="archived" />} />
          <Route path="archived/:id/" element={<MailDetail />} />
          <Route path="compose/" element={<Compose />} />
        </Routes>
      </main>
    </>
  );
}
