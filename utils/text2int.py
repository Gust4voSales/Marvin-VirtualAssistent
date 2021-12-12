num_dict = {
  "zero": 0,
  "um": 1,
  "uma": 1,
  "dois": 2,
  "duas": 2,
  "três": 3,
  "quatro": 4,
  "cinco": 5,
  "seis": 6,
  "sete": 7,
  "oito": 8,
  "nove": 9,

  "dez": 10,
  "onze": 11,
  "doze": 12,
  "treze": 13,
  "quatorze": 14,
  "quinze": 15,
  "dezesseis": 16,
  "dezessete": 17,
  "dezoito": 18,
  "dezenove": 19,

  "vinte": 20,
  "trinta": 30,
  "quarenta": 40,
  "cinquenta": 50,
  "sessenta": 60,
  "setenta": 70,
  "oitenta": 80,
  "noventa": 90,

  "cem": 100,
  "cento": 100 ,
  "duzentos": 200,
  "trezentos": 300,
  "quatrocentos": 400,
  "quinhentos": 500,
  "seiscentos": 600,
  "setecentos": 700,
  "oitocentos": 800,
  "novecentos": 900,
}

milhar_dict = {
  "mil": 1000,
  "milhão": 1000000,
  "milhões": 1000000,
  "bilhão": 1000000000,
  "bilhões": 1000000000,
}

def run(num_text):
  resultado = 0
  grupoCorrente = 0

  for word in num_text.split(' '):
    if word in num_dict:
      grupoCorrente += num_dict[word]
    elif word in milhar_dict:
      if grupoCorrente==0:
        resultado += 1 * milhar_dict[word]
      else:
        grupoCorrente * milhar_dict[word]

  resultado += grupoCorrente
  return resultado
