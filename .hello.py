print('''🗞 Notícia Processo Judicial\n------------------------------\n🏛 Número do Processo: {}\n{}\n💼 Assunto: {}\n👥 Personagens mencionados nos autos: {}\n-----------------------------------------------------------\n📅 Data do Último Andamento: {}\n💬 Último Andamento: {}\n------------------------------\n\n\nSaudações,\n\n      ✨ luiz@peixoto.cc ✨\n\n'''.format(row["Número do Processo"], row["Título do Processo"], row["Assunto"], row["Partes"], row["Data do Último Andamento"], row["Último Andamento"]), file=arquivo)
