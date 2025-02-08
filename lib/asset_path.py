# https://tildagon.badge.emfcamp.org/tildagon-apps/reference/ctx/#adding-images
import os

apps = os.listdir("/apps")
path = ""
ASSET_PATH = "apps//"

if "pikesley_tildagon_emf_cave" in apps:
    ASSET_PATH = "/apps/pikesley_tildagon_emf_cave/"

if "emf_cave" in apps:
    ASSET_PATH = "apps/emf_cave/"
