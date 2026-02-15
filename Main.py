import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { motion } from "framer-motion";

const initialLinks = [
  { id: 1, title: "YouTube — Chaîne Roblox", url: "https://youtube.com/@alpha_roblox-v6o?si=akPvJJR0dHIpiiTi", type: "link" },
  { id: 2, title: "YouTube — Chaîne Fortnite", url: "https://youtube.com/@alpha_fortnite-l5u?si=1E02OfGAw21mn4E9", type: "link" },
  { id: 3, title: "YouTube — Gaming aléatoire", url: "https://youtube.com/@alpha_games30?si=_slgcvNo_UiZhZKO", type: "link" },
  { id: 4, title: "Instagram", url: "https://www.instagram.com/alpha_game30?igsh=OTMzcG9ueGNhdTEw", type: "link" },
  { id: 5, title: "Spotify", url: "https://open.spotify.com/user/31k5ajlsqnxhd3glj3bbc5iirq5i?si=iizxRCU9SeS3wqzL4d0mIQ", type: "link" },
  { id: 6, title: "TikTok", url: "https://www.tiktok.com/@edonis5911?_r=1&_t=ZG-93x6VX3UYBE", type: "link" },
  { id: 7, title: "Discord (moi)", value: "alpha_gaming30", type: "text" },
  { id: 8, title: "Discord (serveur)", url: "https://discord.gg/DBgCn5MxAQ", type: "link" },
  { id: 9, title: "Pokémon GO", value: "663406890740", type: "text" },
  { id: 10, title: "E-mail", url: "mailto:alpha.ytb.contact.me@gmail.com", display: "alpha.ytb.contact.me@gmail.com", type: "link" },
];

export default function LinkHub() {
  const [links, setLinks] = useState(initialLinks);
  const [title, setTitle] = useState("");
  const [url, setUrl] = useState("");

  const addLink = () => {
    if (!title || !url) return;
    setLinks([...links, { id: Date.now(), title, url, type: "link" }]);
    setTitle("");
    setUrl("");
  };

  const removeLink = (id) => {
    setLinks(links.filter((l) => l.id !== id));
  };

  const copyText = (text) => {
    navigator.clipboard.writeText(text);
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-900 via-gray-800 to-black text-white flex flex-col items-center p-6 gap-6">
      {/* Profile Header */}
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="flex flex-col items-center gap-3"
      >
        <div className="w-24 h-24 rounded-full bg-gray-700 flex items-center justify-center text-xl font-bold">
          AG
        </div>
        <h1 className="text-3xl font-bold">Alpha Gaming</h1>
        <p className="text-gray-300 text-center">Mes réseaux et liens officiels</p>
      </motion.div>

      {/* Add link panel */}
      <Card className="w-full max-w-md rounded-2xl bg-gray-800 border-gray-700">
        <CardContent className="p-4 flex flex-col gap-3">
          <Input
            placeholder="Nom du lien"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="bg-gray-900 border-gray-700 text-white"
          />
          <Input
            placeholder="https://..."
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            className="bg-gray-900 border-gray-700 text-white"
          />
          <Button onClick={addLink}>Ajouter le lien</Button>
        </CardContent>
      </Card>

      {/* Links list */}
      <div className="w-full max-w-md flex flex-col gap-4">
        {links.map((link) => (
          <motion.div
            key={link.id}
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            whileHover={{ scale: 1.03 }}
          >
            <Card className="rounded-2xl bg-gray-800 border-gray-700 shadow-lg">
              <CardContent className="p-4 flex justify-between items-center gap-3">
                {link.type === "link" ? (
                  <a
                    href={link.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="font-medium underline break-all"
                  >
                    {link.display || link.title}
                  </a>
                ) : (
                  <span className="font-medium break-all">{link.title}: {link.value}</span>
                )}

                <div className="flex gap-2">
                  {link.type === "text" && (
                    <Button onClick={() => copyText(link.value)}>Copier</Button>
                  )}
                  <Button
                    variant="destructive"
                    onClick={() => removeLink(link.id)}
                  >
                    Supprimer
                  </Button>
                </div>
              </CardContent>
            </Card>
          </motion.div>
        ))}
      </div>
    </div>
  );
}
