#!/bin/bash
# Laddar ner en modell i taget, översätter engelska → språket, tar bort modellen
S=/tmp/claude-0/-home-user-ovningsfabriken/ac359c10-5e45-5417-911d-b8378f720154/scratchpad
C=/home/user/ovningsfabriken/verktyg/sprak/cache
declare -A URL=( [ar]=en_ar-1_0 [fa]=en_fa-1_5 [fi]=en_fi-1_9 [es]=en_es-1_0 [de]=en_de-1_3 [fr]=en_fr-1_9 [pl]=en_pl-1_9 [tr]=en_tr-1_5 [uk]=en_uk-1_4 [ru]=en_ru-1_9 [pt]=en_pt-1_9 [it]=en_it-1_0 )
for l in ${SPRAKLISTA:-de es fr fi ar pl tr uk ru fa pt it}; do
  echo "== $l $(date +%T)"
  d=$S/argos/m_$l; mkdir -p $d
  curl -sSL -o $d/m.zip https://argos-net.com/v1/translate-${URL[$l]}.argosmodel && (cd $d && unzip -o -q m.zip && rm m.zip)
  MB=$(dirname "$(find $d -name model.bin | head -1)"); md=$(dirname "$MB")   # paketets rot: model/ + sentencepiece.model eller bpe.model
  cd $S && python3 mt_run.py $C/en-kalla.json $C/en-$l.json $md en 2>&1 | grep -v "^[0-9]* /" 
  rm -rf $d
done
echo ALLT KLART $(date +%T)
