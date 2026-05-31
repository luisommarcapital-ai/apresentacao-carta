#!/usr/bin/env python3
"""
Scraping do post do Instagram: https://www.instagram.com/p/DZAW7ruHLeR/

Modos de uso:
    # Via sessionid do browser (recomendado — funciona em servidores):
    python3 scrape_instagram.py --sessionid SEU_SESSIONID

    # Via usuário/senha (pode falhar em IPs de datacenter):
    python3 scrape_instagram.py --user SEU_USUARIO --password SUA_SENHA

Como obter o sessionid:
    1. Abra o Instagram no Chrome já logado
    2. F12 → Application → Cookies → https://www.instagram.com
    3. Copie o valor do cookie "sessionid"
"""

import json
import argparse
import sys

try:
    import instaloader
except ImportError:
    sys.exit("Execute: pip install instaloader")

POST_SHORTCODE = "DZAW7ruHLeR"


def scrape_post(username: str = None, password: str = None, sessionid: str = None) -> dict:
    L = instaloader.Instaloader(
        download_pictures=False,
        download_videos=False,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=False,
        quiet=True,
    )

    if sessionid:
        print("Autenticando via sessionid do browser...")
        L.context._session.cookies.update({"sessionid": sessionid})
        L.context.username = username or "user"
    elif username and password:
        print(f"Autenticando como @{username}...")
        L.login(username, password)

    print(f"Buscando post {POST_SHORTCODE}...")
    post = instaloader.Post.from_shortcode(L.context, POST_SHORTCODE)

    data = {
        "shortcode": post.shortcode,
        "url": f"https://www.instagram.com/p/{post.shortcode}/",
        "perfil": {
            "username": post.owner_username,
            "id": post.owner_id,
            "url": f"https://www.instagram.com/{post.owner_username}/",
        },
        "tipo": post.typename,  # GraphImage, GraphVideo, GraphSidecar
        "data_publicacao": post.date_utc.isoformat(),
        "data_local": post.date_local.strftime("%d/%m/%Y %H:%M"),
        "legenda": post.caption,
        "hashtags": list(post.caption_hashtags),
        "mencoes": list(post.caption_mentions),
        "curtidas": post.likes,
        "comentarios": post.comments,
        "acessibilidade": post.accessibility_caption,
        "localizacao": str(post.location) if post.location else None,
        "patrocinado": post.is_sponsored,
        "url_imagem": post.url,
    }

    # Carrossel: múltiplas mídias
    if post.typename == "GraphSidecar":
        data["midias"] = [
            {"url": node.display_url, "tipo": node.typename}
            for node in post.get_sidecar_nodes()
        ]

    return data


def main():
    parser = argparse.ArgumentParser(description="Scraping de post do Instagram")
    parser.add_argument("--user", help="Usuário do Instagram")
    parser.add_argument("--password", help="Senha do Instagram")
    parser.add_argument("--sessionid", help="Cookie sessionid extraído do browser (recomendado)")
    args = parser.parse_args()

    try:
        data = scrape_post(args.user, args.password, args.sessionid)
    except instaloader.exceptions.LoginRequiredException:
        print("\nErro: Este post requer autenticação.")
        print("Use: python3 scrape_instagram.py --sessionid SEU_SESSIONID")
        sys.exit(1)
    except instaloader.exceptions.PostChangedException:
        print("\nErro: Post não encontrado ou removido.")
        sys.exit(1)
    except Exception as e:
        print(f"\nErro: {e}")
        sys.exit(1)

    output_file = f"post_{POST_SHORTCODE}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n=== Post raspado com sucesso ===")
    print(f"Perfil  : @{data['perfil']['username']}")
    print(f"Tipo    : {data['tipo']}")
    print(f"Data    : {data['data_local']}")
    print(f"Curtidas: {data['curtidas']}")
    print(f"Coments : {data['comentarios']}")
    if data.get("hashtags"):
        print(f"Hashtags: {' '.join('#' + h for h in data['hashtags'])}")
    print(f"\nLegenda:\n{data['legenda']}")
    print(f"\nResultado salvo em: {output_file}")


if __name__ == "__main__":
    main()
