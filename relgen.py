import os
import warnings
import pandas as pd
import argparse
import datetime
import subprocess


def format_data(df):
    df["Partes"] = (df["Partes"]
                    .fillna("")
                    .apply(lambda x: ", ".join(list(set(str(x).split(", ")))) if isinstance(x, str) else ""
                    )
                   )

    df["Título do Processo"] = df.apply(
        lambda x: "🚧 Descrição Ausente na Base de Dados do TJRJ" if x["Número do Processo"] in x["Título do Processo"] else x["Título do Processo"],
        axis=1
    )

    df = df.fillna(value="🚧 Descrição ausente na Base de Dados do TJRJ 🚧")
    df = df.loc[:, ["Número do Processo", "Título do Processo", "Assunto", "Partes", "Data do Último Andamento", "Último Andamento"]]

    return df


def generate_report(df, caminho_relatorio):
    with open(caminho_relatorio, "w", encoding="utf-8") as arquivo:
        for index, row in df.iterrows():
            print("-" * 60, file=arquivo)
            print("🏛 Número do Processo:", row["Número do Processo"], file=arquivo)
            print("", row["Título do Processo"], file=arquivo)
            print("💼 Assunto:", row["Assunto"], file=arquivo)
            print("👥 Personagens mencionados nos autos:", row["Partes"], file=arquivo)
            print("-" * 55, file=arquivo)
            print("📅 Data do Último Andamento:", row["Data do Último Andamento"], file=arquivo)
            print(f"💬 Último Andamento: {row['Último Andamento']}", file=arquivo)
            print("-" * 60, file=arquivo)
            print("\n" * 2, file=arquivo)

        print("""Saudações,\n ✨ luiz@peixoto.cc ✨""", file=arquivo)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("nome_do_arquivo", help="nome do arquivo a ser processado")
    args = parser.parse_args()

    nome_do_arquivo = args.nome_do_arquivo
    caminho_arquivo = args.nome_do_arquivo
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d_%H:%M")
    path = "/home/peixoto/Documentos/Relatórios/relgen/"
    nome_relatorio = f"relatorio_{date_string}.txt"
    caminho_relatorio = os.path.join(path, nome_relatorio)

    print(f"\n Processando 🚧 {nome_do_arquivo} 🔥")

    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        df = pd.read_excel(caminho_arquivo, sheet_name="Processos", engine="openpyxl")

    df = format_data(df)

    generate_report(df, caminho_relatorio)

    print(f"\033[32m\nRelatório salvo com sucesso!\033[0m ✨ 🍰 ✨\n\n📂 {caminho_relatorio}\n")
    comando = ["gedit", caminho_relatorio]
    subprocess.Popen(comando)


if __name__ == "__main__":
    main()

