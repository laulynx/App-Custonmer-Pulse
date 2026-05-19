from http.server import BaseHTTPRequestHandler, HTTPServer


HOST = "127.0.0.1"
PORT = 8000


HTML = r"""<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Customer Pulse Brutal</title>
    <style>
      :root {
        --yellow: #fff200;
        --black: #050505;
        --paper: #fffdf1;
        --blue: #0057ff;
        --pink: #ff004c;
        --green: #00e676;
        --cyan: #00d1ff;
        --shadow: 8px 8px 0 var(--black);
        --font: Inter, Arial, Helvetica, sans-serif;
      }

      * {
        box-sizing: border-box;
      }

      body {
        margin: 0;
        min-height: 100vh;
        background:
          linear-gradient(90deg, rgba(5, 5, 5, 0.18) 1px, transparent 1px),
          linear-gradient(rgba(5, 5, 5, 0.18) 1px, transparent 1px),
          var(--yellow);
        background-size: 34px 34px;
        color: var(--black);
        font-family: var(--font);
        letter-spacing: 0;
      }

      .shell {
        display: grid;
        grid-template-columns: 280px minmax(0, 1fr);
        min-height: 100vh;
      }

      aside {
        position: sticky;
        top: 0;
        height: 100vh;
        padding: 24px;
        border-right: 4px solid var(--black);
        background: #fff8d0;
      }

      .brand {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 42px;
        font-weight: 900;
      }

      .brand-mark {
        display: grid;
        width: 48px;
        height: 48px;
        place-items: center;
        border: 3px solid var(--black);
        background: var(--blue);
        color: white;
        box-shadow: 4px 4px 0 var(--black);
      }

      nav {
        display: grid;
        gap: 12px;
      }

      nav a {
        border: 3px solid transparent;
        padding: 14px;
        color: var(--black);
        text-decoration: none;
        font-weight: 900;
      }

      nav a.active,
      nav a:hover {
        border-color: var(--black);
        background: var(--black);
        color: white;
      }

      .risk-box,
      .card,
      .panel {
        border: 4px solid var(--black);
        background: var(--paper);
        box-shadow: var(--shadow);
      }

      .risk-box {
        margin-top: 56px;
        padding: 18px;
      }

      .risk-box strong {
        display: block;
        margin: 8px 0;
        font-size: 1.5rem;
      }

      main {
        padding: 28px;
        overflow: hidden;
      }

      .top {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 24px;
        margin-bottom: 26px;
      }

      .eyebrow {
        margin: 0 0 8px;
        font-family: "Courier New", monospace;
        font-size: 0.75rem;
        font-weight: 900;
        text-transform: uppercase;
      }

      h1 {
        max-width: 980px;
        margin: 0;
        font-size: clamp(3rem, 8vw, 7rem);
        line-height: 0.88;
        font-weight: 1000;
        text-transform: uppercase;
      }

      .status {
        min-width: max-content;
        border: 4px solid var(--black);
        padding: 14px 16px;
        background: var(--pink);
        color: white;
        box-shadow: 5px 5px 0 var(--black);
        font-weight: 1000;
        text-transform: uppercase;
      }

      .hero {
        display: grid;
        grid-template-columns: minmax(280px, 0.9fr) minmax(320px, 1.1fr);
        gap: 20px;
      }

      .card,
      .panel {
        padding: 22px;
      }

      .sentiment-card {
        transform: rotate(-0.45deg);
      }

      .sentiment-head {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 14px;
      }

      .sentiment-head h2 {
        margin: 0;
        font-size: clamp(4rem, 9vw, 7rem);
        line-height: 0.82;
      }

      .tag {
        border: 3px solid var(--black);
        padding: 8px 10px;
        background: var(--green);
        font-family: "Courier New", monospace;
        font-weight: 900;
      }

      .orbit {
        position: relative;
        display: grid;
        width: min(350px, 76vw);
        aspect-ratio: 1;
        margin: 26px auto 12px;
        place-items: center;
      }

      .orbit::before,
      .orbit::after,
      .orbit span {
        content: "";
        position: absolute;
        border-radius: 50%;
      }

      .orbit::before {
        inset: 0;
        border: 18px solid var(--blue);
        clip-path: polygon(50% 50%, 100% 0, 100% 100%, 0 100%, 0 42%);
      }

      .orbit::after {
        inset: 38px;
        border: 18px solid var(--pink);
        clip-path: polygon(50% 50%, 100% 0, 100% 90%, 25% 100%);
        transform: rotate(62deg);
      }

      .orbit span {
        display: grid;
        inset: 96px;
        place-items: center;
        background: var(--black);
        color: white;
        font-family: "Courier New", monospace;
        font-size: 1.2rem;
        font-weight: 900;
      }

      .insight {
        display: grid;
        align-content: space-between;
        min-height: 100%;
        background:
          linear-gradient(135deg, rgba(0, 87, 255, 0.14), transparent 40%),
          var(--paper);
        transform: rotate(0.35deg);
      }

      .insight h2 {
        max-width: 760px;
        margin: 42px 0 26px;
        font-size: clamp(2.8rem, 6vw, 5.8rem);
        line-height: 0.88;
        text-transform: uppercase;
      }

      .insight p {
        max-width: 720px;
        font-size: 1.05rem;
        line-height: 1.55;
      }

      .actions {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
      }

      button {
        border: 4px solid var(--black);
        padding: 13px 18px;
        background: var(--blue);
        color: white;
        box-shadow: 5px 5px 0 var(--black);
        cursor: pointer;
        font: inherit;
        font-weight: 1000;
        text-transform: uppercase;
      }

      button.secondary {
        background: var(--paper);
        color: var(--black);
      }

      .kpis {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 20px;
        margin: 20px 0;
      }

      .kpi:nth-child(2) {
        transform: rotate(0.6deg);
      }

      .kpi:nth-child(3) {
        transform: rotate(-0.5deg);
      }

      .kpi span {
        font-weight: 900;
        text-transform: uppercase;
      }

      .kpi strong {
        display: block;
        margin: 12px 0 8px;
        font-size: clamp(2.2rem, 4vw, 3.8rem);
        line-height: 1;
      }

      .grid {
        display: grid;
        grid-template-columns: minmax(320px, 1.15fr) minmax(280px, 0.85fr);
        gap: 20px;
      }

      .panel-title {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 16px;
        margin-bottom: 22px;
      }

      .panel h2 {
        margin: 0;
        font-size: 1.5rem;
        text-transform: uppercase;
      }

      .bars {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        align-items: end;
        gap: 12px;
        min-height: 250px;
      }

      .bars div {
        display: flex;
        align-items: end;
        justify-content: center;
        height: var(--height);
        min-height: 56px;
        border: 3px solid var(--black);
        background: linear-gradient(180deg, var(--pink), var(--blue));
        color: white;
        font-weight: 1000;
      }

      .segments {
        display: grid;
        gap: 16px;
      }

      .segment {
        display: grid;
        grid-template-columns: 1fr auto;
        gap: 10px;
        align-items: center;
      }

      .bar-track {
        grid-column: 1 / -1;
        height: 16px;
        border: 3px solid var(--black);
        background: white;
      }

      .bar-fill {
        height: 100%;
        width: var(--value);
        background: var(--blue);
      }

      .inbox {
        grid-column: 1 / -1;
      }

      .emails {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 16px;
      }

      .email {
        display: grid;
        grid-template-columns: auto 1fr auto;
        gap: 12px;
        padding: 14px;
        border: 3px solid var(--black);
        background: #fff8d0;
      }

      .avatar {
        display: grid;
        width: 42px;
        height: 42px;
        place-items: center;
        border: 3px solid var(--black);
        background: var(--pink);
        color: white;
        font-weight: 1000;
      }

      .email strong,
      .email b {
        font-weight: 1000;
      }

      .email p {
        margin: 6px 0 0;
        line-height: 1.35;
      }

      @media (max-width: 1060px) {
        .shell {
          grid-template-columns: 1fr;
        }

        aside {
          position: relative;
          height: auto;
        }

        nav {
          grid-template-columns: repeat(5, minmax(max-content, 1fr));
          overflow-x: auto;
        }

        .hero,
        .grid,
        .emails {
          grid-template-columns: 1fr;
        }

        .kpis {
          grid-template-columns: repeat(2, minmax(0, 1fr));
        }
      }

      @media (max-width: 680px) {
        aside,
        main {
          padding: 16px;
        }

        .top,
        .sentiment-head,
        .panel-title {
          display: grid;
        }

        .status {
          min-width: 0;
          width: fit-content;
        }

        .kpis {
          grid-template-columns: 1fr;
        }

        .bars {
          gap: 7px;
        }

        .email {
          grid-template-columns: auto 1fr;
        }

        .email b {
          grid-column: 2;
        }
      }
    </style>
  </head>
  <body>
    <div class="shell">
      <aside>
        <div class="brand">
          <div class="brand-mark">CP</div>
          <div>
            <div>Customer Pulse</div>
            <small>BRUTAL ANALYTICS</small>
          </div>
        </div>

        <nav>
          <a class="active" href="#">Dashboard</a>
          <a href="#">Emails</a>
          <a href="#">Sentimiento</a>
          <a href="#">Clientes</a>
          <a href="#">Alertas</a>
        </nav>

        <section class="risk-box">
          <p class="eyebrow">Riesgo activo</p>
          <strong>18 clientes</strong>
          <div>Frustracion alta y respuesta pendiente.</div>
        </section>
      </aside>

      <main>
        <header class="top">
          <div>
            <p class="eyebrow">Centro de inteligencia de soporte</p>
            <h1>Salud del negocio desde cada email recibido</h1>
          </div>
          <div class="status">Modo brutal</div>
        </header>

        <section class="hero">
          <article class="card sentiment-card">
            <div class="sentiment-head">
              <div>
                <p class="eyebrow">Sentimiento global</p>
                <h2>72%<br />positivo</h2>
              </div>
              <span class="tag">+8.4%</span>
            </div>
            <div class="orbit"><span>1.842</span></div>
          </article>

          <article class="card insight">
            <div>
              <p class="eyebrow">Insight prioritario</p>
              <h2>Facturacion esta generando detractores</h2>
              <p>
                42 emails negativos mencionan cobros, duplicados o tiempos de
                resolucion superiores a 24h. Prioridad recomendada: equipo
                financiero + soporte premium.
              </p>
            </div>
            <div class="actions">
              <button>Crear alerta</button>
              <button class="secondary">Ver segmentos</button>
            </div>
          </article>
        </section>

        <section class="kpis">
          <article class="card kpi">
            <span>Emails recibidos</span>
            <strong>8.293</strong>
            <small>+14% vs. periodo anterior</small>
          </article>
          <article class="card kpi">
            <span>Tiempo respuesta</span>
            <strong>3h 18m</strong>
            <small>-41m esta semana</small>
          </article>
          <article class="card kpi">
            <span>Clientes nuevos</span>
            <strong>426</strong>
            <small>86 con alto potencial</small>
          </article>
          <article class="card kpi">
            <span>Abandonados</span>
            <strong>37</strong>
            <small>12 recuperables</small>
          </article>
        </section>

        <section class="grid">
          <article class="panel">
            <div class="panel-title">
              <div>
                <p class="eyebrow">Respuesta y volumen</p>
                <h2>Actividad semanal</h2>
              </div>
              <span class="tag">SLA 91%</span>
            </div>
            <div class="bars">
              <div style="--height: 42%">Lu</div>
              <div style="--height: 64%">Ma</div>
              <div style="--height: 56%">Mi</div>
              <div style="--height: 78%">Ju</div>
              <div style="--height: 92%">Vi</div>
              <div style="--height: 38%">Sa</div>
              <div style="--height: 31%">Do</div>
            </div>
          </article>

          <article class="panel">
            <div class="panel-title">
              <div>
                <p class="eyebrow">Promotores vs detractores</p>
                <h2>Segmentos</h2>
              </div>
              <span class="tag">NPS +38</span>
            </div>
            <div class="segments">
              <div class="segment">
                <strong>Promotores</strong><b>312</b>
                <div class="bar-track"><div class="bar-fill" style="--value: 76%"></div></div>
              </div>
              <div class="segment">
                <strong>Neutrales</strong><b>184</b>
                <div class="bar-track"><div class="bar-fill" style="--value: 44%"></div></div>
              </div>
              <div class="segment">
                <strong>Detractores</strong><b>69</b>
                <div class="bar-track"><div class="bar-fill" style="--value: 22%"></div></div>
              </div>
            </div>
          </article>

          <article class="panel inbox">
            <div class="panel-title">
              <div>
                <p class="eyebrow">Emails criticos</p>
                <h2>Detractores potenciales</h2>
              </div>
              <span class="tag">Urgente</span>
            </div>
            <div class="emails">
              <article class="email">
                <div class="avatar">AM</div>
                <div>
                  <strong>Ana Martinez</strong>
                  <p>Factura duplicada y tercera reclamacion sin respuesta.</p>
                </div>
                <b>-0.82</b>
              </article>
              <article class="email">
                <div class="avatar">RC</div>
                <div>
                  <strong>Rafa Castro</strong>
                  <p>Quiere cancelar si no se resuelve la migracion hoy.</p>
                </div>
                <b>-0.64</b>
              </article>
              <article class="email">
                <div class="avatar">LV</div>
                <div>
                  <strong>Lucia Vidal</strong>
                  <p>Recomendaria el producto tras el ultimo onboarding.</p>
                </div>
                <b>+0.91</b>
              </article>
            </div>
          </article>
        </section>
      </main>
    </div>
  </body>
</html>"""


class BrutalDashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode("utf-8"))

    def log_message(self, format, *args):
        return


def run_server():
    server = HTTPServer((HOST, PORT), BrutalDashboardHandler)
    print(f"Dashboard brutal disponible en http://{HOST}:{PORT}")
    print("Pulsa Ctrl+C para detener el servidor.")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
