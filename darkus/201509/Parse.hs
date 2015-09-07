module Parse where

import Ant (Ant(..), AntList)
import Change (Change(..))

import qualified Text.Parsec as P

charToAnt :: Char -> Ant
charToAnt c
  | c == 'К'  = K
  | c == 'Л'  = L
  | c == 'П'  = P
  | c == 'Х'  = H

numbers :: String
numbers = "0123456789"

is_num :: Char -> Bool
is_num x = x `elem` numbers

antChars     = "КЛПХ"
deleteString = "удл"
pasteString  = "вст"
changeString = "изм"

type ActionType = (String, String, Char)
actionParser :: P.Parsec String () ActionType
actionParser = do
  change <- P.try (deleteParser) P.<|> P.try (pasteParser) P.<|> changeParser
  return change

deleteParser = do
  digits <- P.many1 P.digit
  word <- P.string deleteString
  return (word, digits, 'X')

pasteParser = do
  digits <- P.many1 P.digit
  word <- P.string pasteString
  char <- P.oneOf antChars
  return (word, digits, char)

changeParser = do
  digits <- P.many1 P.digit
  word <- P.string changeString
  char <- P.oneOf antChars
  return (word, digits, char)

parse rule text = P.parse rule "(source)" text

actionToChange :: String -> Maybe Change
actionToChange string = case parse actionParser string of
  Left e -> Nothing
  Right (word, digits, char) -> Just (actionToChange' word digits char)

actionToChange' w d c
    | w == deleteString  = Delete n
    | w == pasteString  = Paste n a
    | w == changeString = Change n a
    where n = read d :: Int
          a = charToAnt c

lineParser :: P.Parsec String () (String, ActionType)
lineParser = do
  ants <- P.many1 (P.oneOf antChars)
  P.char ':'
  P.spaces
  res <- actionParser
  return (ants, res)

lineToAntsAction :: String -> Maybe (AntList, Change)
lineToAntsAction string = case parse lineParser string of
  Left e -> Nothing
  Right (as, (w, d, c)) -> Just (ants, action)
    where ants = map charToAnt as
          action = actionToChange' w d c


