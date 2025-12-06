from config_loader import load_config

def main():
    cfg = load_config()
    print(cfg)
    print(cfg["app"]["name"])
    print(cfg["app"].get("version"))

if __name__ == '__main__':
    main()
