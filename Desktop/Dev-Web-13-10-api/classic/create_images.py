import os

assets_img = 'assets/img'
uploads = 'uploads'
os.makedirs(assets_img, exist_ok=True)
os.makedirs(uploads, exist_ok=True)

svgs = {
    'smartphone.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_sp" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f1f5f9"/><stop offset="100%" stop-color="#e2e8f0"/>
    </linearGradient>
    <linearGradient id="body_sp" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/><stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="screen_sp" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/><stop offset="50%" stop-color="#6366f1"/><stop offset="100%" stop-color="#ec4899"/>
    </linearGradient>
    <filter id="sh_sp" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#0f172a" flood-opacity="0.22"/>
    </filter>
  </defs>
  <rect width="400" height="300" rx="16" fill="url(#bg_sp)"/>
  <rect x="135" y="28" width="130" height="244" rx="26" fill="url(#body_sp)" filter="url(#sh_sp)" stroke="#475569" stroke-width="2"/>
  <rect x="141" y="35" width="118" height="230" rx="20" fill="url(#screen_sp)"/>
  <circle cx="200" cy="115" r="40" fill="rgba(255,255,255,0.22)"/>
  <circle cx="220" cy="95" r="20" fill="rgba(255,255,255,0.25)"/>
  <text x="200" y="160" font-family="system-ui, sans-serif" font-size="20" font-weight="800" fill="#ffffff" text-anchor="middle">5G</text>
  <rect x="165" y="180" width="70" height="7" rx="3.5" fill="rgba(255,255,255,0.85)"/>
  <rect x="175" y="194" width="50" height="6" rx="3" fill="rgba(255,255,255,0.6)"/>
  <rect x="182" y="41" width="36" height="10" rx="5" fill="#0f172a"/>
  <rect x="180" y="258" width="40" height="3" rx="1.5" fill="#ffffff" opacity="0.9"/>
  <rect x="16" y="16" width="110" height="24" rx="12" fill="#0284c7" fill-opacity="0.15"/>
  <text x="71" y="32" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0369a1" text-anchor="middle">SMARTPHONE</text>
</svg>''',

    'ordinateur.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_lp" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc"/><stop offset="100%" stop-color="#e2e8f0"/>
    </linearGradient>
    <linearGradient id="scr_lp" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0ea5e9"/><stop offset="60%" stop-color="#2563eb"/><stop offset="100%" stop-color="#4f46e5"/>
    </linearGradient>
    <linearGradient id="al_lp" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#cbd5e1"/><stop offset="100%" stop-color="#94a3b8"/>
    </linearGradient>
    <filter id="sh_lp" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#0f172a" flood-opacity="0.2"/>
    </filter>
  </defs>
  <rect width="400" height="300" rx="16" fill="url(#bg_lp)"/>
  <g filter="url(#sh_lp)">
    <rect x="75" y="42" width="250" height="155" rx="10" fill="#1e293b" stroke="#475569" stroke-width="2"/>
    <rect x="83" y="50" width="234" height="139" rx="6" fill="url(#scr_lp)"/>
    <circle cx="200" cy="110" r="32" fill="rgba(255,255,255,0.2)"/>
    <polygon points="190,95 218,110 190,125" fill="rgba(255,255,255,0.9)"/>
    <circle cx="200" cy="46" r="2.5" fill="#64748b"/>
    <path d="M 45 204 L 355 204 L 335 235 L 65 235 Z" fill="url(#al_lp)" stroke="#64748b" stroke-width="1"/>
    <rect x="170" y="204" width="60" height="4" rx="2" fill="#475569"/>
    <rect x="165" y="214" width="70" height="15" rx="3" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>
  </g>
  <rect x="16" y="16" width="145" height="24" rx="12" fill="#2563eb" fill-opacity="0.15"/>
  <text x="88" y="32" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#1d4ed8" text-anchor="middle">ORDINATEUR PORTABLE</text>
</svg>''',

    'casque.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_hp" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc"/><stop offset="100%" stop-color="#e2e8f0"/>
    </linearGradient>
    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24"/><stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <filter id="sh_hp" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#0f172a" flood-opacity="0.2"/>
    </filter>
  </defs>
  <rect width="400" height="300" rx="16" fill="url(#bg_hp)"/>
  <g filter="url(#sh_hp)">
    <path d="M 120 155 C 120 70, 280 70, 280 155" fill="none" stroke="#1e293b" stroke-width="16" stroke-linecap="round"/>
    <path d="M 140 120 C 150 90, 250 90, 260 120" fill="none" stroke="#475569" stroke-width="8" stroke-linecap="round"/>
    <g transform="translate(100, 140)">
      <rect x="-18" y="0" width="36" height="75" rx="18" fill="#0f172a" stroke="url(#gold)" stroke-width="3"/>
      <circle cx="0" cy="37" r="10" fill="url(#gold)"/>
    </g>
    <g transform="translate(300, 140)">
      <rect x="-18" y="0" width="36" height="75" rx="18" fill="#0f172a" stroke="url(#gold)" stroke-width="3"/>
      <circle cx="0" cy="37" r="10" fill="url(#gold)"/>
    </g>
    <path d="M 60 160 C 50 170, 50 185, 60 195" fill="none" stroke="#0284c7" stroke-width="3" stroke-linecap="round"/>
    <path d="M 70 150 C 55 165, 55 190, 70 205" fill="none" stroke="#0284c7" stroke-width="3" stroke-linecap="round" opacity="0.6"/>
    <path d="M 340 160 C 350 170, 350 185, 340 195" fill="none" stroke="#0284c7" stroke-width="3" stroke-linecap="round"/>
    <path d="M 330 150 C 345 165, 345 190, 330 205" fill="none" stroke="#0284c7" stroke-width="3" stroke-linecap="round" opacity="0.6"/>
  </g>
  <rect x="16" y="16" width="115" height="24" rx="12" fill="#d97706" fill-opacity="0.15"/>
  <text x="73" y="32" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#b45309" text-anchor="middle">CASQUE AUDIO</text>
</svg>''',

    'montre.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_wt" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc"/><stop offset="100%" stop-color="#e2e8f0"/>
    </linearGradient>
    <linearGradient id="scr_wt" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <filter id="sh_wt" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#0f172a" flood-opacity="0.2"/>
    </filter>
  </defs>
  <rect width="400" height="300" rx="16" fill="url(#bg_wt)"/>
  <g filter="url(#sh_wt)">
    <path d="M 170 20 L 230 20 L 225 80 L 175 80 Z" fill="#334155"/>
    <path d="M 175 220 L 225 220 L 230 280 L 170 280 Z" fill="#334155"/>
    <rect x="145" y="75" width="110" height="150" rx="32" fill="#1e293b" stroke="#64748b" stroke-width="3"/>
    <rect x="152" y="82" width="96" height="136" rx="26" fill="url(#scr_wt)"/>
    <circle cx="200" cy="150" r="42" fill="none" stroke="#22c55e" stroke-width="6" stroke-dasharray="180 80"/>
    <circle cx="200" cy="150" r="32" fill="none" stroke="#06b6d4" stroke-width="5" stroke-dasharray="140 60"/>
    <circle cx="200" cy="150" r="22" fill="none" stroke="#f43f5e" stroke-width="4" stroke-dasharray="100 40"/>
    <text x="200" y="146" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">10:42</text>
    <text x="200" y="162" font-family="system-ui, sans-serif" font-size="9" font-weight="600" fill="#94a3b8" text-anchor="middle">128 BPM</text>
    <rect x="255" y="110" width="8" height="22" rx="4" fill="#64748b"/>
  </g>
  <rect x="16" y="16" width="140" height="24" rx="12" fill="#16a34a" fill-opacity="0.15"/>
  <text x="86" y="32" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#15803d" text-anchor="middle">MONTRE CONNECTÉE</text>
</svg>''',

    'tablette.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_tb" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc"/><stop offset="100%" stop-color="#e2e8f0"/>
    </linearGradient>
    <linearGradient id="scr_tb" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#8b5cf6"/><stop offset="50%" stop-color="#ec4899"/><stop offset="100%" stop-color="#f97316"/>
    </linearGradient>
    <filter id="sh_tb" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#0f172a" flood-opacity="0.2"/>
    </filter>
  </defs>
  <rect width="400" height="300" rx="16" fill="url(#bg_tb)"/>
  <g filter="url(#sh_tb)">
    <rect x="90" y="35" width="220" height="230" rx="20" fill="#0f172a" stroke="#475569" stroke-width="2"/>
    <rect x="98" y="43" width="204" height="214" rx="14" fill="url(#scr_tb)"/>
    <circle cx="200" cy="140" r="50" fill="rgba(255,255,255,0.25)"/>
    <rect x="140" y="195" width="120" height="8" rx="4" fill="rgba(255,255,255,0.8)"/>
    <rect x="160" y="210" width="80" height="6" rx="3" fill="rgba(255,255,255,0.6)"/>
    <circle cx="200" cy="39" r="2" fill="#64748b"/>
    <!-- Stylus Pen -->
    <rect x="316" y="80" width="6" height="130" rx="3" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>
    <polygon points="316,210 322,210 319,222" fill="#475569"/>
  </g>
  <rect x="16" y="16" width="95" height="24" rx="12" fill="#9333ea" fill-opacity="0.15"/>
  <text x="63" y="32" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#7e22ce" text-anchor="middle">TABLETTE</text>
</svg>''',

    'camera.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_cm" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc"/><stop offset="100%" stop-color="#e2e8f0"/>
    </linearGradient>
    <linearGradient id="lens_cm" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/><stop offset="40%" stop-color="#0f172a"/><stop offset="80%" stop-color="#1e1b4b"/><stop offset="100%" stop-color="#10b981"/>
    </linearGradient>
    <filter id="sh_cm" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#0f172a" flood-opacity="0.2"/>
    </filter>
  </defs>
  <rect width="400" height="300" rx="16" fill="url(#bg_cm)"/>
  <g filter="url(#sh_cm)">
    <rect x="90" y="85" width="220" height="140" rx="16" fill="#1e293b" stroke="#334155" stroke-width="2"/>
    <rect x="90" y="85" width="55" height="140" rx="12" fill="#0f172a" opacity="0.6"/>
    <path d="M 160 85 L 180 60 L 220 60 L 240 85 Z" fill="#1e293b"/>
    <rect x="250" y="72" width="25" height="12" rx="3" fill="#475569"/>
    <circle cx="262" cy="78" r="3" fill="#ef4444"/>
    <circle cx="200" cy="155" r="56" fill="#0f172a" stroke="#64748b" stroke-width="4"/>
    <circle cx="200" cy="155" r="44" fill="url(#lens_cm)" stroke="#e2e8f0" stroke-width="1.5"/>
    <ellipse cx="185" cy="140" rx="18" ry="10" fill="rgba(255,255,255,0.35)" transform="rotate(-30 185 140)"/>
    <ellipse cx="215" cy="170" rx="8" ry="4" fill="rgba(255,255,255,0.2)" transform="rotate(-30 215 170)"/>
    <circle cx="120" cy="110" r="6" fill="#f59e0b"/>
  </g>
  <rect x="16" y="16" width="90" height="24" rx="12" fill="#dc2626" fill-opacity="0.15"/>
  <text x="61" y="32" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#b91c1c" text-anchor="middle">CAMÉRA</text>
</svg>''',

    'placeholder.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="100%" height="100%">
  <defs>
    <linearGradient id="bg_ph" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc"/><stop offset="100%" stop-color="#e2e8f0"/>
    </linearGradient>
  </defs>
  <rect width="400" height="300" rx="16" fill="url(#bg_ph)"/>
  <circle cx="200" cy="125" r="50" fill="#cbd5e1" opacity="0.5"/>
  <path d="M 180 145 L 195 125 L 210 145 L 225 120 L 245 155 L 155 155 Z" fill="#94a3b8"/>
  <circle cx="180" cy="110" r="8" fill="#94a3b8"/>
  <text x="200" y="205" font-family="system-ui, sans-serif" font-size="15" font-weight="700" fill="#64748b" text-anchor="middle">PRODUIT HIGH-TECH</text>
  <text x="200" y="226" font-family="system-ui, sans-serif" font-size="12" fill="#94a3b8" text-anchor="middle">Boutique Classic</text>
</svg>'''
}

for name, content in svgs.items():
    with open(os.path.join(assets_img, name), 'w', encoding='utf-8') as f:
        f.write(content.strip())
    # Copie dans uploads pour que image_p puisse pointer dessus
    with open(os.path.join(uploads, name), 'w', encoding='utf-8') as f:
        f.write(content.strip())

print('Les 7 fichiers SVG d images produits ont ete crees avec succes !')
