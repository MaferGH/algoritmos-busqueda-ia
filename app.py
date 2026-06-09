import streamlit as st
import time as _time
import sys
sys.path.insert(0, '.')

st.set_page_config(page_title="Proyecto Búsquedas",
                   layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');
*,*::before,*::after{box-sizing:border-box;}
html,body,[class*="css"]{font-family:'DM Sans',Arial,sans-serif!important;background:#fff!important;color:#1a1a1a!important;}
#MainMenu,footer,header,[data-testid="stToolbar"],[data-testid="stDecoration"],
[data-testid="stStatusWidget"],[data-testid="collapsedControl"],
[data-testid="stSidebar"]{display:none!important;height:0!important;}
.main{padding:0!important;}
.main .block-container{padding:0!important;margin:0!important;max-width:100%!important;}
section[data-testid="stMain"]{padding:0!important;}
.topbar{position:fixed;top:0;left:0;right:0;z-index:500;height:52px;background:#fff;
  border-bottom:1.5px solid #f0f0f0;display:flex;align-items:center;padding:0 1.1rem;gap:10px;}
.tbar-title{font-size:.95rem;font-weight:600;flex:1;}
.tbar-sub{font-size:.68rem;color:#aaa;font-family:'DM Mono',monospace;}
[data-testid="stRadio"]{margin:0!important;padding:0!important;}
[data-testid="stRadio"]>label{display:none!important;}
[data-testid="stRadio"]>div{display:flex!important;flex-direction:row!important;gap:0!important;width:100%!important;background:transparent!important;}
[data-testid="stRadio"]>div>label{flex:1!important;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;min-height:60px!important;padding:6px 2px 10px!important;cursor:pointer!important;border-radius:0!important;background:transparent!important;}
[data-testid="stRadio"]>div>label>div:first-child{display:none!important;}
[data-testid="stRadio"]>div>label>div:last-child{font-size:.6rem!important;font-weight:500!important;color:#bbb!important;text-align:center!important;white-space:pre-line!important;}
[data-testid="stRadio"]>div>label[data-baseweb="radio"]:has(input:checked)>div:last-child{color:#1a1a1a!important;font-weight:700!important;}
div[data-testid="stRadio"]:last-of-type{position:fixed!important;bottom:0!important;left:0!important;right:0!important;z-index:500!important;background:rgba(255,255,255,.97)!important;border-top:1.5px solid #f0f0f0!important;margin:0!important;padding:0!important;}
.scroll{position:fixed;top:52px;left:0;right:0;bottom:60px;overflow-y:auto;overflow-x:hidden;background:#fff;-webkit-overflow-scrolling:touch;}
.page{max-width:680px;margin:0 auto;padding:1rem .9rem .8rem;}
.stitle{font-size:.62rem;font-weight:600;color:#aaa;text-transform:uppercase;letter-spacing:.7px;margin:.85rem 0 .4rem;}
.card{background:#fff;border:1.5px solid #f0f0f0;border-radius:12px;margin-bottom:.55rem;overflow:hidden;}
.card-body{padding:.8rem .95rem;}
.tag{display:inline-block;border-radius:20px;padding:2px 9px;font-size:.62rem;font-weight:600;}
.t-ok{background:#edfaf1;color:#1a7f3c;} .t-err{background:#fff0f0;color:#c0392b;} .t-neu{background:#f0f4ff;color:#2563eb;}
.msg-box{background:#f8f8f8;border-left:3px solid #1a1a1a;border-radius:0 8px 8px 0;padding:.65rem .85rem;
  font-family:'DM Mono',monospace;font-size:.72rem;line-height:1.6;color:#222;white-space:pre-wrap;margin-top:.5rem;}
.mrow{display:grid;grid-template-columns:repeat(auto-fill,minmax(80px,1fr));gap:.4rem;margin-top:.45rem;}
.mbox{background:#f8f8f8;border-radius:8px;padding:.45rem .6rem;text-align:center;}
.mval{font-family:'DM Mono',monospace;font-size:.9rem;font-weight:600;color:#1a1a1a;}
.mlbl{font-size:.55rem;font-weight:500;color:#aaa;text-transform:uppercase;letter-spacing:.5px;margin-top:1px;}
[data-testid="stSelectbox"]>label{display:none!important;}
[data-testid="stSelectbox"]>div>div{border:1.5px solid #ebebeb!important;border-radius:9px!important;background:#fafafa!important;font-size:.87rem!important;}
[data-testid="stSlider"]{padding:0!important;}
[data-testid="stSlider"]>label{display:none!important;}
[data-testid="stSlider"]>div>div>div{background:#e0e0e0!important;}
[data-testid="stSlider"]>div>div>div>div{background:#1a1a1a!important;}
[data-testid="stSlider"]>div>div>div>div>div{background:#1a1a1a!important;border:2px solid #fff!important;box-shadow:0 1px 4px rgba(0,0,0,.18)!important;width:20px!important;height:20px!important;}
[data-testid="stCaptionContainer"]{font-family:'DM Mono',monospace!important;color:#bbb!important;font-size:.68rem!important;text-align:center!important;margin-top:.15rem!important;}
[data-testid="stCheckbox"]>label{font-size:.85rem!important;}
div[data-testid="stButton"]>button{background:#1a1a1a!important;color:#fff!important;border:none!important;border-radius:10px!important;
  font-family:'DM Sans',Arial,sans-serif!important;font-size:.88rem!important;font-weight:600!important;
  padding:.65rem 1rem!important;width:100%!important;transition:opacity .12s!important;}
div[data-testid="stButton"]>button:hover{opacity:.85!important;}
hr{border:none!important;border-top:1.5px solid #f0f0f0!important;margin:.65rem 0!important;}
.search-grid{border-collapse:collapse;margin:.3rem auto;}
.search-grid td{width:54px;height:54px;text-align:center;vertical-align:middle;
  border:1px solid #ddd;font-family:'DM Mono',monospace;font-size:.65rem;transition:all .2s;padding:2px;}
.gc-wall{background:#555;color:#fff;font-weight:700;font-size:.85rem;}
.gc-start{background:#bbdefb;color:#0d47a1;border:2px solid #1565c0;}
.gc-goal{background:#ffe082;color:#5d4037;border:2px solid #ffa000;}
.gc-current{background:#1a1a1a;color:#fff;border:2px solid #1a1a1a;font-weight:700;}
.gc-open{background:#fff9c4;color:#5d4037;border:2px solid #fbc02d;}
.gc-closed{background:#e3f2fd;color:#1565c0;border:1.5px solid #90caf9;}
.gc-path{background:#c8e6c9;color:#1b5e20;border:2px solid #4caf50;}
.gc-free{background:#fafafa;color:#555;border:1px solid #e0e0e0;}
.gc-coord{font-size:.55rem;color:inherit;display:block;font-weight:600;}
.gc-hval{font-size:.58rem;color:inherit;display:block;opacity:.85;}
.ttt{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;max-width:210px;margin:.4rem auto;}
.tc{aspect-ratio:1;border-radius:10px;display:flex;align-items:center;justify-content:center;
  font-size:1.3rem;font-weight:700;border:1.5px solid #f0f0f0;background:#f9f9f9;transition:all .18s;}
.tc-X{color:#2563eb;background:#eff6ff;border-color:#bfdbfe;}
.tc-O{color:#dc2626;background:#fff5f5;border-color:#fecaca;}
.tc-mt{color:#ccc;font-size:.65rem;font-weight:400;}
.tc-eval{background:#fffbeb;border-color:#fcd34d;}
.tc-best{background:#f0fdf4;border-color:#4ade80;border-width:2px;}
.tc-win{border-width:3px!important;transform:scale(1.06);}
.tc-X.tc-win{border-color:#1d4ed8!important;background:#dbeafe!important;}
.tc-O.tc-win{border-color:#b91c1c!important;background:#fee2e2!important;}
.ev-row{display:flex;align-items:center;justify-content:space-between;padding:4px 8px;border-radius:7px;margin:2px 0;font-family:'DM Mono',monospace;font-size:.72rem;}
.ev-win{background:#edfaf1;color:#1a7f3c;} .ev-draw{background:#f5f5f5;color:#888;} .ev-lose{background:#fff0f0;color:#c0392b;} .ev-best{border:1.5px solid #4ade80;}
.ttt-game{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;max-width:240px;margin:.5rem auto;}
.tg-cell{aspect-ratio:1;border-radius:12px;display:flex;align-items:center;justify-content:center;
  font-size:1.5rem;font-weight:700;border:2px solid #e0e0e0;background:#f9f9f9;transition:all .2s;}
.tg-X{color:#2563eb;background:#eff6ff;border-color:#93c5fd;}
.tg-O{color:#dc2626;background:#fff5f5;border-color:#fca5a5;}
.tg-empty{color:#ddd;font-size:.75rem;background:#fff;}
.tg-win-X{background:#dbeafe!important;border-color:#1d4ed8!important;border-width:3px!important;}
.tg-win-O{background:#fee2e2!important;border-color:#b91c1c!important;border-width:3px!important;}
.queens{display:grid;grid-template-columns:repeat(8,1fr);gap:3px;padding:.3rem 0;}
.qc{aspect-ratio:1;border-radius:4px;display:flex;align-items:center;justify-content:center;font-size:.8rem;font-weight:700;transition:all .2s;}
.ql{background:#f7f7f7;} .qd{background:#e8e8e8;}
.qs{background:#edfaf1!important;color:#1a7f3c;}
.qk{background:#fff0f0!important;color:#c0392b;}
.qm{background:#dbeafe!important;color:#1e40af;border:2px solid #93c5fd;}
.maze{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;padding:.3rem 0;max-width:270px;margin:0 auto;}
.mc{aspect-ratio:1;border-radius:9px;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:'DM Mono',monospace;transition:all .18s;}
.mc-letter{font-size:.85rem;font-weight:700;line-height:1;}
.mc-coord{font-size:.42rem;opacity:.35;margin-top:2px;font-weight:400;}
.fl-S{background:#e3f2fd;border:2px solid #1565c0;} .fl-S .mc-letter{color:#0d47a1;}
.fl-F{background:#e8f4fd;border:1.5px solid #bbdefb;} .fl-F .mc-letter{color:#1565c0;}
.fl-H{background:#1a1a1a;border:1.5px solid #000;} .fl-H .mc-letter{color:#fff;}
.fl-G{background:#fff9c4;border:2px solid #fdd835;} .fl-G .mc-letter{color:#f57f17;}
.fl-cur{background:#1a1a1a;border:2px solid #1a1a1a;transform:scale(1.07);} .fl-cur .mc-letter{color:#fff;}
.fl-trail{background:#bbdefb;border:1.5px solid #90caf9;} .fl-trail .mc-letter{color:#0d47a1;}
.fl-path{background:#c8e6c9;border:2px solid #66bb6a;} .fl-path .mc-letter{color:#1b5e20;}
.legend{display:flex;gap:.35rem;flex-wrap:wrap;margin-top:.4rem;}
.leg-item{font-size:.62rem;padding:2px 7px;border-radius:4px;font-family:'DM Mono',monospace;}
.result-ok{background:#edfaf1;border:2px solid #4ade80;border-radius:10px;padding:.8rem;text-align:center;margin:.5rem 0;}
.result-lose{background:#fff0f0;border:2px solid #f87171;border-radius:10px;padding:.8rem;text-align:center;margin:.5rem 0;}
.result-draw{background:#f8f8f8;border:2px solid #e0e0e0;border-radius:10px;padding:.8rem;text-align:center;margin:.5rem 0;}
</style>
""", unsafe_allow_html=True)

from busqueda_no_informada import bfs, dfs, LABERINTO, INICIO, META
from busqueda_informada    import (a_star, greedy_bfs, GRID,
                                    INICIO as INF_INICIO, META as INF_META,
                                    FILAS, COLS)
from busqueda_local        import (hill_climbing, simulated_annealing,
                                    estado_aleatorio, celdas_en_conflicto)
from busqueda_adversaria   import (minimax_wrapper, alphabeta_wrapper, VACIO,
                                    X as TTT_X, O as TTT_O,
                                    computadora_juega, etiqueta_puntaje,
                                    verificar_ganador, juego_terminado,
                                    tablero_lleno, linea_ganadora,
                                    hacer_jugada, celdas_libres,
                                    mostrar_tablero)

CATS = {
    "No informada": {
        "tipo": "laberinto", "prob": "Frozen Lake 4×4",
        "algos": {
            "BFS": "Cola FIFO — nivel por nivel.\nGarantiza el camino más corto.",
            "DFS": "Pila LIFO — profundidad primero.\nNo garantiza el óptimo.",
        }
    },
    "Informada": {
        "tipo": "grid", "prob": "Manhattan Gridworld 4×7",
        "algos": {
            "A*":                "f = g + h. Óptimo y completo.\nHeurística: distancia Manhattan.",
            "Greedy Best-First": "Solo h(n). Rápido.\nPuede no ser el camino más corto.",
        }
    },
    "Local": {
        "tipo": "reinas", "prob": "8 Reinas",
        "algos": {
            "Hill Climbing":       "Siempre al vecino con menos conflictos.\nPuede atascarse en óptimo local.",
            "Recosido Simulado": "Acepta peores con probabilidad.\nEscapa de óptimos locales.",
        }
    },
    "Adversaria": {
        "tipo": "ttt", "prob": "Tic-Tac-Toe (Gato)",
        "algos": {
            "Minimax":    "Árbol completo de juego.\nComputadora (X) nunca pierde.",
            "Alpha-Beta": "Minimax + poda α-β.\nMisma decisión perfecta, más eficiente.",
        }
    },
}

PROS_CONS = {
    "BFS":("Camino más corto garantizado","Usa mucha memoria"),
    "DFS":("Muy poca memoria","No garantiza el óptimo"),
    "A*":("Óptimo con h admisible","Más memoria que Greedy"),
    "Greedy Best-First":("Generalmente rápido","No garantiza el óptimo"),
    "Hill Climbing":("Simple y rápido","Se atasca en óptimos locales"),
    "Recosido Simulado":("Escapa de óptimos locales","Parámetros críticos"),
    "Minimax":("Nunca pierde — decisión perfecta","Lento en juegos grandes"),
    "Alpha-Beta":("Mismo resultado que Minimax, más rápido","Más complejo"),
}

DEFS = {
    "tab":"Inicio", "sel_cat":"No informada", "sel_alg":None,
    "cmp_on":False, "sel_alg2":None, "modo_juego":False,
    "resultado":None, "alg":None, "tipo":None, "ms":None,
    "resultado2":None, "alg2":None, "ms2":None,
    "paso":0,
    "estado_ini_reinas":None,
    "juego_tablero":[VACIO]*9, "juego_terminado":False,
    "juego_ganador":None, "juego_algoritmo":"Minimax",
    "juego_turno":"X",
    "juego_msg":"",
    "juego_analisis":[],
    "juego_activo":False,
}
for k, v in DEFS.items():
    if k not in st.session_state:
        st.session_state[k] = v

def render_maze_frozen(pasos, hasta):
    trail = set()
    for i in range(min(hasta+1, len(pasos))):
        c = pasos[i].get("celda")
        if c: trail.add(tuple(c))
    info   = pasos[hasta]
    celda  = tuple(info.get("celda") or (0,0))
    camino = set(tuple(x) for x in (info.get("camino") or [])) if info.get("tipo")=="solucion" else set()
    h = '<div class="maze">'
    for i in range(4):
        for j in range(4):
            c = (i,j)
            if LABERINTO[i][j]==1:            cls,letra="mc fl-H","H"
            elif c==tuple(META):              cls,letra="mc fl-G"+(" fl-cur" if c==celda else ""),"G"
            elif c==celda:                    cls,letra="mc fl-cur","●"
            elif c in camino:                 cls,letra="mc fl-path","F"
            elif c in trail and c!=celda:     cls,letra="mc fl-trail","F"
            elif c==INICIO:                   cls,letra="mc fl-S","S"
            else:                             cls,letra="mc fl-F","F"
            h+=f'<div class="{cls}"><div class="mc-letter">{letra}</div><div class="mc-coord">{i},{j}</div></div>'
    return h+'</div>'


def render_grid_informada(info):
    celda   = info.get("celda", INF_INICIO)
    open_   = info.get("open_set", {})
    closed  = set(tuple(x) if isinstance(x,(list,tuple)) else x for x in info.get("closed_set",[]))
    camino  = set(tuple(x) for x in info.get("camino",[]))
    h_grid  = info.get("h_grid", {})

    h = '<div style="overflow-x:auto"><table class="search-grid">'
    for i in range(FILAS):
        h += '<tr>'
        for j in range(COLS):
            c = (i,j)
            hv = h_grid.get(c, "")
            if GRID[i][j]==1:
                h += '<td class="gc-wall">X</td>'
            elif c==tuple(INF_META):
                h += f'<td class="gc-goal"><span class="gc-coord">F</span><span class="gc-hval">h=0</span></td>'
            elif c==tuple(INF_INICIO):
                h += f'<td class="gc-start"><span class="gc-coord">I</span><span class="gc-hval">h={hv}</span></td>'
            elif c==celda:
                h += f'<td class="gc-current"><span class="gc-coord">★</span><span class="gc-hval">h={hv}</span></td>'
            elif c in camino and c not in closed:
                h += f'<td class="gc-path"><span class="gc-coord">{i},{j}</span><span class="gc-hval">h={hv}</span></td>'
            elif c in open_:
                fv = round(open_[c],1) if isinstance(open_[c],float) else open_[c]
                h += f'<td class="gc-open"><span class="gc-coord">{i},{j}</span><span class="gc-hval">h={hv}|f={fv}</span></td>'
            elif c in closed:
                h += f'<td class="gc-closed"><span class="gc-coord">{i},{j}</span><span class="gc-hval">h={hv} ✓</span></td>'
            else:
                h += f'<td class="gc-free"><span class="gc-coord">{i},{j}</span><span class="gc-hval">h={hv}</span></td>'
        h += '</tr>'
    h += '</table></div>'
    h += '''<div class="legend">
        <span class="leg-item" style="background:#bbdefb;color:#0d47a1;border:1px solid #1565c0">I=Inicio</span>
        <span class="leg-item" style="background:#ffe082;color:#5d4037;border:1px solid #ffa000">F=Meta</span>
        <span class="leg-item" style="background:#1a1a1a;color:#fff">X=Muro</span>
        <span class="leg-item" style="background:#fff9c4;color:#5d4037;border:1px solid #fbc02d">OPEN</span>
        <span class="leg-item" style="background:#e3f2fd;color:#1565c0;border:1px solid #90caf9">CLOSED</span>
        <span class="leg-item" style="background:#c8e6c9;color:#1b5e20;border:1px solid #4caf50">Camino</span>
    </div>'''
    return h


def render_ttt_analisis(info):
    board = info.get("tablero",[VACIO]*9)
    best  = info.get("mejor_movimiento")
    pe    = info.get("pos_evaluada")
    linea = set(info.get("linea_ganadora") or [])
    h = '<div class="ttt">'
    for i, v in enumerate(board):
        en_l = i in linea
        if v==TTT_X:   cls="tc tc-X"+(" tc-win" if en_l else ""); c="X"
        elif v==TTT_O: cls="tc tc-O"+(" tc-win" if en_l else ""); c="O"
        elif i==pe:    cls="tc tc-mt tc-eval"; c=str(i)
        elif i==best:  cls="tc tc-mt tc-best"; c=str(i)
        else:          cls="tc tc-mt"; c=str(i)
        h += f'<div class="{cls}">{c}</div>'
    h += '</div>'
    if linea:
        ln=sorted(linea); gano=board[ln[0]]; color="#2563eb" if gano==TTT_X else "#dc2626"
        TM={frozenset([0,1,2]):"fila 1 (horizontal)",frozenset([3,4,5]):"fila 2 (horizontal)",
            frozenset([6,7,8]):"fila 3 (horizontal)",frozenset([0,3,6]):"columna 1 (vertical)",
            frozenset([1,4,7]):"columna 2 (vertical)",frozenset([2,5,8]):"columna 3 (vertical)",
            frozenset([0,4,8]):"diagonal ↘",frozenset([2,4,6]):"diagonal ↙"}
        tp=TM.get(frozenset(ln),"línea")
        h+=f'<div style="text-align:center;margin-top:.4rem;font-size:.82rem;font-weight:600;color:{color}">¡{gano} gana por {tp}!</div>'
    movs=info.get("movimientos_evaluados",[])
    if movs:
        h+='<div style="margin-top:.5rem"><div class="stitle" style="margin:.25rem 0">Evaluación — ¿por qué elige cada posición?</div>'
        for pos,val in movs:
            ec="ev-win" if val>0 else("ev-lose" if val<0 else "ev-draw")
            bc=" ev-best" if pos==best else ""
            lbl=etiqueta_puntaje(val)
            arr=" ← ELEGIDA" if pos==best else ""
            vs=f"+{val}" if val>0 else str(val)
            h+=f'<div class="ev-row {ec}{bc}"><span>Pos {pos}: {vs}</span><span style="font-size:.65rem">{lbl}{arr}</span></div>'
        h+='</div>'
        # Nota explicativa
        h+='<div style="font-size:.7rem;color:#888;margin-top:.4rem;font-style:italic">'
        h+='Nota: "+9" = X gana con 3 en línea en ESTA jugada.<br>'
        h+='"+ 7" = X FORZARÁ 3 en línea en los próximos movimientos (aunque O juegue perfecto).<br>'
        h+='"0" = Empate garantizado. Estos valores no son L-formas: siempre se gana con 3 en línea.</div>'
    return h


def render_reinas(info):
    estado  = info.get("estado",[])
    if not estado: return ""
    n       = len(estado)
    en_conf = set(info.get("en_conflicto") or celdas_en_conflicto(estado))
    mov_f   = info.get("reina_movida",-1)
    h = '<div class="queens">'
    for i in range(n):
        for j in range(n):
            base = "ql" if (i+j)%2==0 else "qd"
            if estado[i]==j:
                if i==mov_f:     ex=" qm"
                elif i in en_conf: ex=" qk"
                else:              ex=" qs"
                h+=f'<div class="qc {base}{ex}">Q</div>'
            else: h+=f'<div class="qc {base}"></div>'
    h+='</div>'
    fm=info.get("reina_movida",-1); ca=info.get("col_anterior",-1); cn=info.get("col_nueva",-1)
    if fm>=0 and ca!=cn:
        h+=f'<div style="font-size:.75rem;color:#2563eb;margin-top:.3rem;font-family:monospace">Reina fila {fm}: columna {ca} → columna {cn}</div>'
    h+='<div class="legend" style="margin-top:.3rem">'
    h+='<span class="leg-item" style="background:#edfaf1;color:#1a7f3c">Q verde=sin conflicto</span>'
    h+='<span class="leg-item" style="background:#fff0f0;color:#c0392b">Q roja=conflicto</span>'
    h+='<span class="leg-item" style="background:#dbeafe;color:#1e40af">Q azul=se movió</span>'
    h+='</div>'
    return h


def metrics_row(info):
    ks=[("nodos","Nodos"),("costo","Costo"),("g","g(n)"),("h","h(n)"),("f","f(n)"),
        ("conflictos","Conflictos"),("iteracion","Iter."),("temperatura","Temp."),("valor","Valor")]
    items=[(l,info[k]) for k,l in ks if k in info and info[k] is not None]
    if not items: return ""
    h='<div class="mrow">'
    for l,v in items:
        if isinstance(v,float): v=round(v,3)
        h+=f'<div class="mbox"><div class="mval">{v}</div><div class="mlbl">{l}</div></div>'
    return h+'</div>'


def historial(pasos, hasta):
    TLBL={"expansion":"Expande","solucion":"✓ Meta","fracaso":"✗ Fallo",
          "inicio":"Inicio","movimiento":"Mueve","fin_ok":"✓ Solución",
          "fin":"Fin","evaluacion":"Evalúa","decision":"Decide"}
    ini=max(0,hasta-5)
    h='<div>'
    for i in range(ini,min(hasta+1,len(pasos))):
        p=pasos[i]; tp=p.get("tipo","")
        dc="ok" if tp in("solucion","fin_ok") else("err" if tp in("fracaso","fin") else("cur" if i==hasta else ""))
        lbl=TLBL.get(tp,tp)
        desc=p.get("mensaje","").split("\n")[0][:55]
        bold=' style="font-weight:600"' if i==hasta else ''
        col={"ok":"#4ade80","err":"#f87171","cur":"#1a1a1a"}.get(dc,"#ddd")
        h+=f'<div style="display:flex;align-items:flex-start;gap:8px;padding:.28rem 0;border-bottom:1px solid #f5f5f5;font-size:.76rem;color:#444"><div style="font-family:monospace;font-size:.58rem;color:#bbb;min-width:20px;margin-top:4px">{i+1}</div><div style="width:7px;height:7px;border-radius:50%;background:{col};flex-shrink:0;margin-top:5px"></div><div{bold}><span style="color:#aaa;margin-right:4px">{lbl}</span>{desc}</div></div>'
    return h+'</div>'


def vizblock(pasos, paso, tipo):
    info=pasos[paso]
    if tipo=="laberinto":   viz=render_maze_frozen(pasos,paso)
    elif tipo=="grid":      viz=render_grid_informada(info)
    elif tipo=="ttt":       viz=render_ttt_analisis(info)
    elif tipo=="reinas":    viz=render_reinas(info)
    else:                   viz=""
    tlbl={"expansion":"Expansión","solucion":"Solución","fracaso":"Sin solución",
          "inicio":"Estado inicial","movimiento":"Movimiento","fin_ok":"¡Solución!",
          "fin":"Fin","evaluacion":"Evaluando jugada","decision":"Decisión"}.get(info.get("tipo",""),"Paso")
    msg=info.get("mensaje","")
    met=metrics_row(info)
    ghf=""
    if tipo=="grid" and "g" in info:
        g,hh,f=info.get("g","?"),info.get("h","?"),info.get("f","?")
        if isinstance(f,float): f=round(f,2)
        if isinstance(hh,float): hh=round(hh,2)
        ghf=f'<div style="font-family:monospace;font-size:.73rem;background:#eef4ff;border-radius:7px;padding:.3rem .7rem;margin-top:.4rem;color:#2563eb">g={g}  +  h={hh}  =  f={f}</div>'
    hist=historial(pasos,paso)
    msg_div = f'<div class="msg-box">{msg}</div>' if msg else ""
    return f'<div class="stitle">{tlbl}</div>{viz}{ghf}{msg_div}{met}<div class="stitle" style="margin-top:.75rem">Historial</div>{hist}'


def resumen_final(pasos, met, alg, tipo):
    n_exp=sum(1 for p in pasos if p.get("tipo")=="expansion")
    n_mov=sum(1 for p in pasos if p.get("tipo")=="movimiento")
    n_eval=sum(1 for p in pasos if p.get("tipo")=="evaluacion")
    sol=any(p.get("tipo") in("solucion","fin_ok") for p in pasos)
    pro,con=PROS_CONS.get(alg,("—","—"))
    h='<div class="card"><div class="card-body">'
    h+=f'<div style="font-weight:600;font-size:.95rem;margin-bottom:.5rem">Desglose: {alg}</div>'
    h+='<div class="mrow">'
    h+=f'<div class="mbox"><div class="mval">{len(pasos)}</div><div class="mlbl">Pasos totales</div></div>'
    if n_exp: h+=f'<div class="mbox"><div class="mval">{n_exp}</div><div class="mlbl">Expandidos</div></div>'
    if n_mov: h+=f'<div class="mbox"><div class="mval">{n_mov}</div><div class="mlbl">Movimientos</div></div>'
    if n_eval:h+=f'<div class="mbox"><div class="mval">{n_eval}</div><div class="mlbl">Evaluados</div></div>'
    for k,v in met.items():
        if v is not None: h+=f'<div class="mbox"><div class="mval">{v}</div><div class="mlbl">{k}</div></div>'
    h+='</div>'
    h+=f'<div style="margin-top:.6rem"><div style="font-size:.75rem;color:#1a7f3c;margin-bottom:2px">✓ Ventaja: {pro}</div>'
    h+=f'<div style="font-size:.75rem;color:#c0392b">✗ Desventaja: {con}</div></div>'
    h+='</div></div>'
    return h


def resumen_comparacion(alg1,pasos1,met1,ms1,alg2,pasos2,met2,ms2):
    sol1=any(p.get("tipo") in("solucion","fin_ok") for p in pasos1)
    sol2=any(p.get("tipo") in("solucion","fin_ok") for p in pasos2)
    ganador=alg1 if ms1<=ms2 else alg2
    h='<div class="card"><div class="card-body">'
    h+='<div style="font-weight:600;font-size:.95rem;margin-bottom:.5rem">Comparación final</div>'
    h+='<table style="width:100%;border-collapse:collapse;font-size:.78rem">'
    h+=f'<tr style="background:#f8f8f8"><th style="text-align:left;padding:4px 8px">Métrica</th>'
    h+=f'<th style="text-align:center;padding:4px 8px">{alg1}</th>'
    h+=f'<th style="text-align:center;padding:4px 8px">{alg2}</th></tr>'
    filas=[("Tiempo ms",ms1,ms2),("Pasos totales",len(pasos1),len(pasos2)),
           ("Solución","Sí" if sol1 else "No","Sí" if sol2 else "No")]
    for k,v1 in met1.items():
        v2=met2.get(k)
        if v1 is not None and v2 is not None: filas.append((k,v1,v2))
    for i,(label,v1,v2) in enumerate(filas):
        bg="#fff" if i%2==0 else "#fafafa"
        h+=f'<tr style="background:{bg}"><td style="padding:4px 8px">{label}</td>'
        h+=f'<td style="text-align:center;padding:4px 8px">{v1}</td>'
        h+=f'<td style="text-align:center;padding:4px 8px">{v2}</td></tr>'
    h+=f'</table><div style="margin-top:.5rem;font-size:.78rem">⚡ Más rápido: <strong>{ganador}</strong></div>'
    h+='</div></div>'
    return h

def render_tablero_juego(board, linea_win=None):
    """HTML-only board for display (X, O, empty with number)."""
    linea_set = set(linea_win or [])
    h = '<div class="ttt-game">'
    for i in range(9):
        v = board[i]; en_l = i in linea_set
        if v == TTT_X:
            h += f'<div class="tg-cell tg-X{" tg-win-X" if en_l else ""}">X</div>'
        elif v == TTT_O:
            h += f'<div class="tg-cell tg-O{" tg-win-O" if en_l else ""}">O</div>'
        else:
            h += f'<div class="tg-cell tg-empty">{i}</div>'
    h += '</div>'
    return h


def render_board_clickable(board, terminado, turno, usar_ab, analisis, ganador):
    """
    Renders the 3×3 TTT board using Streamlit columns.
    X and O cells are HTML. Empty cells are Streamlit buttons (clickable).
    Returns True if a move was made (triggers rerun).
    """
    linea = linea_ganadora(board) if terminado else None
    linea_set = set(linea or [])
    moved = False

    for row in range(3):
        cols = st.columns(3, gap="small")
        for col in range(3):
            pos = row * 3 + col
            val = board[pos]
            en_l = pos in linea_set
            with cols[col]:
                if val == TTT_X:
                    bg = "#dbeafe" if en_l else "#eff6ff"
                    bc = "#1d4ed8" if en_l else "#93c5fd"
                    bw = "3px" if en_l else "2px"
                    st.markdown(f'''<div style="background:{bg};border:{bw} solid {bc};border-radius:12px;
                        height:76px;display:flex;align-items:center;justify-content:center;
                        font-size:1.6rem;font-weight:700;color:#2563eb;margin-bottom:4px">X</div>''',
                        unsafe_allow_html=True)
                elif val == TTT_O:
                    bg = "#fee2e2" if en_l else "#fff5f5"
                    bc = "#b91c1c" if en_l else "#fca5a5"
                    bw = "3px" if en_l else "2px"
                    st.markdown(f'''<div style="background:{bg};border:{bw} solid {bc};border-radius:12px;
                        height:76px;display:flex;align-items:center;justify-content:center;
                        font-size:1.6rem;font-weight:700;color:#dc2626;margin-bottom:4px">O</div>''',
                        unsafe_allow_html=True)
                else:
                    if not terminado and turno == TTT_O:
                        clicked = st.button("", key=f"cell_{pos}",
                                            use_container_width=True,
                                            help=f"Jugar O en celda {pos}")
                        if clicked:
                            board[pos] = TTT_O
                            st.session_state.juego_tablero = board[:]

                            if juego_terminado(board):
                                st.session_state.juego_terminado = True
                                g = verificar_ganador(board)
                                st.session_state.juego_ganador = g if g else "empate"
                                st.rerun()
                            mejor_pos, mejor_punt, evals = computadora_juega(board, usar_ab)
                            if mejor_pos is not None:
                                board[mejor_pos] = TTT_X
                                st.session_state.juego_tablero = board[:]
                                signo = "+" if mejor_punt > 0 else ""
                                partes = [f"  Pos {p}: {'+' if v>0 else ''}{v} → {etiqueta_puntaje(v)}" for p,v in evals]
                                evals_str = chr(10).join(partes)
                                msg = ("X evalúa posiciones:" + chr(10) + evals_str + chr(10)*2 +
                                       f"X elige posición {mejor_pos} → {etiqueta_puntaje(mejor_punt)}")
                                st.session_state.juego_analisis.append(msg)
                                if juego_terminado(board):
                                    st.session_state.juego_terminado = True
                                    g = verificar_ganador(board)
                                    st.session_state.juego_ganador = g if g else "empate"
                            moved = True
                            st.rerun()
                    else:
                        st.markdown(f'''<div style="background:#fafafa;border:2px dashed #e0e0e0;
                            border-radius:12px;height:76px;display:flex;align-items:center;
                            justify-content:center;font-size:.75rem;color:#ddd;
                            margin-bottom:4px">{pos}</div>''',
                            unsafe_allow_html=True)
    return moved


def pantalla_juego():
    board     = st.session_state.juego_tablero[:]
    terminado = st.session_state.juego_terminado
    ganador   = st.session_state.juego_ganador
    algoritmo = st.session_state.juego_algoritmo
    analisis  = st.session_state.juego_analisis
    turno     = st.session_state.juego_turno
    usar_ab   = (algoritmo == "Alpha-Beta")
    st.markdown("""
    <style>
    div[data-testid="stHorizontalBlock"] div[data-testid="stButton"] > button {
        height: 76px !important;
        background: #fafafa !important;
        border: 2px dashed #d0d0d0 !important;
        border-radius: 12px !important;
        color: #bbb !important;
        font-size: .7rem !important;
        font-weight: 400 !important;
        margin-bottom: 4px !important;
    }
    div[data-testid="stHorizontalBlock"] div[data-testid="stButton"] > button:hover {
        border-color: #dc2626 !important;
        background: #fff5f5 !important;
        color: #dc2626 !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    tag_cls = "t-ok" if ganador == "empate" else ("t-err" if ganador == TTT_X else "t-neu")
    st.markdown(f"""
    <div class="card"><div class="card-body">
      <div style="display:flex;align-items:center;justify-content:space-between">
        <div>
          <div style="font-weight:700;font-size:1rem;margin-bottom:2px">Gato — {algoritmo}</div>
          <div style="font-size:.72rem;color:#aaa">
            Tú = <span style="color:#dc2626;font-weight:600">O</span> &nbsp;|&nbsp;
            Computadora = <span style="color:#2563eb;font-weight:600">X</span> &nbsp;|&nbsp;
            Toca una celda vacía para jugar
          </div>
        </div>
        <span class="tag {tag_cls}">{"🏁 Fin" if terminado else "🎮 Jugando"}</span>
      </div>
    </div></div>
    """, unsafe_allow_html=True)
    if analisis:
        st.markdown(f"""
        <div class="card"><div class="card-body">
          <div class="stitle">Razonamiento de la computadora (X)</div>
          <div class="msg-box">{analisis[-1]}</div>
        </div></div>
        """, unsafe_allow_html=True)
    st.markdown('<div class="card"><div class="card-body">', unsafe_allow_html=True)

    if not terminado and turno == TTT_O:
        st.markdown('<div style="font-size:.72rem;color:#aaa;text-align:center;margin-bottom:.4rem">Tu turno (O) — toca una celda vacía</div>', unsafe_allow_html=True)

    render_board_clickable(board, terminado, turno, usar_ab, analisis, ganador)
    st.markdown('</div></div>', unsafe_allow_html=True)

    if terminado:
        if ganador == TTT_X:
            st.markdown('''<div class="result-lose">
              <div style="font-size:1.1rem;font-weight:700;color:#c0392b">❌ La computadora (X) ganó</div>
              <div style="font-size:.78rem;color:#888;margin-top:.2rem">Minimax garantiza que X nunca pierde ✓</div>
            </div>''', unsafe_allow_html=True)
        elif ganador == TTT_O:
            st.markdown('''<div class="result-ok">
              <div style="font-size:1.1rem;font-weight:700;color:#1a7f3c">¡Ganaste! (O)</div>
              <div style="font-size:.78rem;color:#888;margin-top:.2rem">Mmm... algo está mal con el algoritmo </div>
            </div>''', unsafe_allow_html=True)
        else:
            st.markdown('''<div class="result-draw">
              <div style="font-size:1.1rem;font-weight:700">Empate </div>
              <div style="font-size:.78rem;color:#888;margin-top:.2rem">Minimax garantiza al menos empate para X ✓</div>
            </div>''', unsafe_allow_html=True)

    st.markdown('<div style="height:.5rem"></div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Nueva partida", key="btn_nueva", use_container_width=True):
            board_nuevo = [VACIO] * 9
            st.session_state.juego_tablero  = board_nuevo[:]
            st.session_state.juego_terminado= False
            st.session_state.juego_ganador  = None
            st.session_state.juego_analisis = []
            # X juega primero automáticamente
            pos0, punt0, evs0 = computadora_juega(board_nuevo, usar_ab)
            if pos0 is not None:
                board_nuevo[pos0] = TTT_X
                partes0 = [f"  Pos {p}: {'+' if v>0 else ''}{v} → {etiqueta_puntaje(v)}" for p,v in evs0]
                estr = chr(10).join(partes0)
                st.session_state.juego_analisis = [
                    f"X abre en posición {pos0} (tablero vacío: todos valen igual)" + chr(10) + estr
                ]
            st.session_state.juego_tablero = board_nuevo[:]
            st.session_state.juego_turno   = TTT_O
            st.rerun()
    with c2:
        if st.button("Ver análisis estático", key="btn_analisis", use_container_width=True):
            # Cargar análisis estático si no existe
            if st.session_state.resultado is None or st.session_state.tipo != "ttt":
                if usar_ab:
                    p_st, m_st = alphabeta_wrapper()
                else:
                    p_st, m_st = minimax_wrapper()
                st.session_state.resultado = {"pasos": p_st, "metricas": m_st}
                st.session_state.alg  = algoritmo
                st.session_state.tipo = "ttt"
                st.session_state.ms   = 0
                st.session_state.paso = 0
            st.session_state.juego_activo = False
            st.rerun()

has = st.session_state.resultado is not None or st.session_state.juego_activo
if st.session_state.juego_activo:
    sub = f"Jugando — {st.session_state.juego_algoritmo}"
elif has:
    sub = f"{st.session_state.alg} · {len(st.session_state.resultado['pasos'])} pasos"
else:
    sub = "Selecciona y ejecuta"
st.markdown(f'<div class="topbar"><div class="tbar-title">Proyecto Búsquedas</div><div class="tbar-sub">{sub}</div></div><div class="scroll"><div class="page">', unsafe_allow_html=True)

tab = st.session_state.tab

if tab == "Inicio":
    st.markdown('<div style="text-align:center;padding:1.2rem 0 1rem"><div style="font-size:2rem;margin-bottom:.4rem"></div><div style="font-size:1.3rem;font-weight:600;margin-bottom:.3rem">Proyecto Búsquedas</div><div style="font-size:.82rem;color:#aaa;line-height:1.6">García Hernández María Fernanda<br>Mora Olvera Abraham</div></div>', unsafe_allow_html=True)
    ICONS={"No informada":"⬡","Informada":"◈","Local":"◇","Adversaria":"◎"}
    for cn,cv in CATS.items():
        n=len(cv["algos"])
        st.markdown(f'<div class="card" style="display:flex;align-items:center;gap:12px;padding:.85rem 1rem"><div style="font-size:1.1rem">{ICONS[cn]}</div><div style="flex:1"><div style="font-weight:600;font-size:.9rem">{cn}</div><div style="font-size:.7rem;color:#aaa">{cv["prob"]} · {n} algoritmos</div></div><div style="color:#ccc">›</div></div>', unsafe_allow_html=True)
        if st.button(f"→ {cn}", key=f"home_{cn}", use_container_width=True):
            st.session_state.sel_cat=cn; st.session_state.tab="Algoritmos"; st.rerun()

elif tab == "Algoritmos":

    cat=CATS[st.session_state.sel_cat]; algos=cat["algos"]
    st.markdown('<div class="stitle">Algoritmo</div>', unsafe_allow_html=True)
    alg_opts=list(algos.keys())
    idx=alg_opts.index(st.session_state.sel_alg) if st.session_state.sel_alg in alg_opts else 0
    alg_s=st.selectbox("alg",alg_opts,index=idx,key="sb_alg",label_visibility="collapsed")
    if alg_s!=st.session_state.sel_alg:
        st.session_state.sel_alg=alg_s; st.rerun()
    if st.session_state.sel_alg:
        st.markdown(f'<div class="msg-box" style="border-color:#bbb">{algos[st.session_state.sel_alg]}</div>', unsafe_allow_html=True)

    es_adv = (st.session_state.sel_cat == "Adversaria")
    if es_adv:
        modo_j = st.checkbox("Jugar contra la computadora (tú = O, PC = X)", value=st.session_state.modo_juego, key="chk_juego")
        if modo_j != st.session_state.modo_juego:
            st.session_state.modo_juego=modo_j; st.rerun()

    if not (es_adv and st.session_state.modo_juego):
        cmp=st.checkbox("Comparar con otro algoritmo", value=st.session_state.cmp_on, key="chk_cmp")
        if cmp!=st.session_state.cmp_on:
            st.session_state.cmp_on=cmp; st.rerun()
        if st.session_state.cmp_on:
            st.markdown('<div class="stitle">Segundo algoritmo</div>', unsafe_allow_html=True)
            idx2=alg_opts.index(st.session_state.sel_alg2) if st.session_state.sel_alg2 in alg_opts else 0
            alg_s2=st.selectbox("alg2",alg_opts,index=idx2,key="sb_alg2",label_visibility="collapsed")
            if alg_s2!=st.session_state.sel_alg2:
                st.session_state.sel_alg2=alg_s2; st.rerun()

    st.markdown('<div style="height:.4rem"></div>', unsafe_allow_html=True)

    if st.button("▶  Ejecutar", key="btn_run", use_container_width=True):
        alg_s=st.session_state.sel_alg; tipo=cat["tipo"]

        if not alg_s:
            st.warning("Selecciona un algoritmo.")
        elif es_adv and st.session_state.modo_juego:
            st.session_state.juego_algoritmo  = alg_s
            st.session_state.juego_tablero    = [VACIO]*9
            st.session_state.juego_terminado  = False
            st.session_state.juego_ganador    = None
            st.session_state.juego_analisis   = []
            st.session_state.juego_activo     = True
            usar_ab = (alg_s == "Alpha-Beta")
            mejor_pos, mejor_punt, evals = computadora_juega([VACIO]*9, usar_ab)
            board_ini = [VACIO]*9
            if mejor_pos is not None:
                board_ini[mejor_pos] = TTT_X
                evals_str = "\n".join(
                    f"  Pos {p}: {'+' if v>0 else ''}{v}  →  {etiqueta_puntaje(v)}"
                    for p, v in evals
                )
                msg = f"X abre en posición {mejor_pos} (todos los valores son iguales con tablero vacío)\n\n{evals_str}"
                st.session_state.juego_analisis = [msg]
            st.session_state.juego_tablero = board_ini
            st.session_state.juego_turno   = TTT_O
            st.session_state.tab           = "Visualizar"
            st.rerun()
        else:
            estado_ini_compartido = None
            if tipo == "reinas":
                estado_ini_compartido = estado_aleatorio()
                st.session_state.estado_ini_reinas = estado_ini_compartido[:]

            def _run(a, t):
                t0 = _time.time()
                if t == "laberinto":
                    if a=="BFS": p,m=bfs()
                    else: p,m=dfs()
                elif t == "grid":
                    if a=="A*": p,m=a_star()
                    else: p,m=greedy_bfs()
                elif t == "reinas":
                    e = estado_ini_compartido if estado_ini_compartido else estado_aleatorio()
                    if a=="Hill Climbing": p,m=hill_climbing(e)
                    else: p,m=simulated_annealing(e)
                else:
                    if a=="Minimax": p,m=minimax_wrapper()
                    else: p,m=alphabeta_wrapper()
                return {"pasos":p,"metricas":m}, round((_time.time()-t0)*1000,1)

            with st.spinner("Calculando…"):
                res,ms=_run(alg_s,tipo)
            st.session_state.resultado=res; st.session_state.alg=alg_s
            st.session_state.tipo=tipo; st.session_state.ms=ms
            st.session_state.paso=0; st.session_state.juego_activo=False

            if st.session_state.cmp_on and st.session_state.sel_alg2:
                with st.spinner(f"Calculando {st.session_state.sel_alg2}…"):
                    res2,ms2=_run(st.session_state.sel_alg2,tipo)
                st.session_state.resultado2=res2; st.session_state.alg2=st.session_state.sel_alg2; st.session_state.ms2=ms2
            else:
                st.session_state.resultado2=None; st.session_state.alg2=None; st.session_state.ms2=None
            st.session_state.tab="Visualizar"; st.rerun()

elif tab == "Visualizar":
    if st.session_state.juego_activo:
        pantalla_juego()

    elif st.session_state.resultado is None:
        st.markdown('<div class="card"><div class="card-body" style="text-align:center;padding:2.5rem 1rem"><div style="font-size:2.5rem">🔍</div><div style="font-weight:600;margin:.4rem 0 .3rem">Sin datos</div><div style="font-size:.8rem;color:#aaa">Ve a Algoritmos y presiona Ejecutar</div></div></div>', unsafe_allow_html=True)
    else:
        res=st.session_state.resultado; res2=st.session_state.resultado2
        tipo=st.session_state.tipo; alg=st.session_state.alg; ms=st.session_state.ms
        pasos=res["pasos"]; met=res["metricas"]
        is_cmp=(res2 is not None)

        if is_cmp:
            pasos2=res2["pasos"]; met2=res2["metricas"]
            alg2=st.session_state.alg2; ms2=st.session_state.ms2
            max_p=max(len(pasos),len(pasos2)); paso=st.session_state.paso
            win=alg if ms<=ms2 else alg2
            sol1=any(p.get("tipo") in("solucion","fin_ok") for p in pasos)
            sol2=any(p.get("tipo") in("solucion","fin_ok") for p in pasos2)
            if tipo=="reinas":
                e=st.session_state.get("estado_ini_reinas")
                if e:
                    st.markdown(f'<div style="font-size:.72rem;color:#2563eb;margin-bottom:.4rem">✓ Ambos algoritmos usan el mismo estado inicial: {e}</div>', unsafe_allow_html=True)

            st.markdown(f'<div class="card"><div class="card-body"><div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:.4rem"><div style="font-weight:600;font-size:.92rem">Comparando: {alg} vs {alg2}</div><span class="tag t-neu">⚡ {win}</span></div><div class="mrow"><div class="mbox"><div class="mval">{ms} ms</div><div class="mlbl">{alg}</div></div><div class="mbox"><div class="mval">{ms2} ms</div><div class="mlbl">{alg2}</div></div><div class="mbox"><div class="mval">{abs(ms-ms2):.1f}</div><div class="mlbl">Dif ms</div></div><div class="mbox"><div class="mval">{len(pasos)}/{len(pasos2)}</div><div class="mlbl">Pasos</div></div></div></div></div>', unsafe_allow_html=True)

            nuevo=st.slider("cmp",0,max_p-1,paso,key="sl_cmp",label_visibility="collapsed")
            if nuevo!=paso: st.session_state.paso=nuevo; st.rerun()
            st.caption(f"Paso {paso+1} / {max_p}  —  arrastra para avanzar")

            ca,cb=st.columns(2,gap="small")
            for col,r,a,mms,sol in[(ca,res,alg,ms,sol1),(cb,res2,alg2,ms2,sol2)]:
                with col:
                    ps=r["pasos"]; idx=min(paso,len(ps)-1)
                    tc="t-ok" if sol else "t-err"; tt="Sol." if sol else "No sol."
                    st.markdown(f'<div class="card"><div class="card-body" style="padding:.6rem .8rem"><div style="font-weight:600;font-size:.82rem;margin-bottom:3px">{a}</div><span class="tag {tc}">{tt}</span><span style="font-size:.62rem;color:#aaa;font-family:monospace;margin-left:5px">{mms} ms</span></div></div><div class="card"><div class="card-body">{vizblock(ps,idx,tipo)}</div></div>', unsafe_allow_html=True)

            if paso>=max_p-1:
                st.markdown(resumen_comparacion(alg,pasos,met,ms,alg2,pasos2,met2,ms2), unsafe_allow_html=True)
        else:
            paso=st.session_state.paso; total=len(pasos)
            sol=any(p.get("tipo") in("solucion","fin_ok") for p in pasos)
            tc="t-ok" if sol else "t-err"; tt="Solución" if sol else "Sin solución"
            st.markdown(f'<div class="card"><div class="card-body"><div style="display:flex;align-items:center;justify-content:space-between"><div><div style="font-weight:700;font-size:1rem;margin-bottom:2px">{alg}</div><div style="font-size:.68rem;color:#aaa;font-family:monospace">{ms} ms · {total} pasos</div></div><span class="tag {tc}">{tt}</span></div></div></div>', unsafe_allow_html=True)

            nuevo=st.slider("viz",0,total-1,paso,key="sl_viz",label_visibility="collapsed")
            if nuevo!=paso: st.session_state.paso=nuevo; st.rerun()
            st.caption(f"Paso {paso+1} / {total}  —  arrastra para avanzar")

            st.markdown(f'<div class="card"><div class="card-body">{vizblock(pasos,paso,tipo)}</div></div>', unsafe_allow_html=True)

            if paso>=total-1:
                st.markdown(resumen_final(pasos,met,alg,tipo), unsafe_allow_html=True)

elif tab=="Info":
    st.markdown('<div style="font-weight:600;font-size:1.05rem;margin-bottom:.7rem">Algoritmos por categoría</div>', unsafe_allow_html=True)
    for cn,cv in CATS.items():
        st.markdown(f'<div class="card"><div class="card-body"><div style="font-weight:600;font-size:.9rem;margin-bottom:.4rem">{cn} <span style="font-size:.7rem;font-weight:400;color:#aaa">· {cv["prob"]}</span></div>', unsafe_allow_html=True)
        for ak,desc in cv["algos"].items():
            pro,con=PROS_CONS.get(ak,("—","—"))
            st.markdown(f'<div style="border-top:1px solid #f3f3f3;padding:.4rem 0"><div style="font-weight:600;font-size:.82rem;margin-bottom:1px">{ak}</div><div style="font-size:.72rem;color:#666;white-space:pre-line;margin-bottom:3px">{desc}</div><div style="font-size:.68rem;color:#1a7f3c">✓ {pro}</div><div style="font-size:.68rem;color:#c0392b">✗ {con}</div></div>', unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)
NAV={"Inicio":"⌂\nInicio","Algoritmos":"⬡\nAlgoritmos","Visualizar":"◈\nVisualizar","Info":"◎\nInfo"}
opts=list(NAV.values()); keys=list(NAV.keys())
cur_idx=keys.index(st.session_state.tab) if st.session_state.tab in keys else 0
sel=st.radio("nav",opts,index=cur_idx,horizontal=True,key="navbar",label_visibility="collapsed")
new_tab=keys[opts.index(sel)]
if new_tab!=st.session_state.tab:
    st.session_state.tab=new_tab; st.rerun()
