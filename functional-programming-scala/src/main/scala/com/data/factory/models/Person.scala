package com.data.factory.models

import com.data.factory.exceptions.{FieldValidatorException, ModelException}
import com.data.factory.utils.FieldValidator

import java.time.format.DateTimeFormatter
import java.time.{Duration, LocalDate, Year}
import scala.util.matching.Regex

class Person  (
  val name: String,
  val birthDate: String,
  val address: String
) extends Serializable {

  val isValid: Boolean = try {
      val validator: FieldValidator = new FieldValidator
      validator.validStringField("name")(name)

      val dateRegex: Regex = "\\d{4}-\\d{2}-\\d{2}".r
      validator.validStringField("birthDate")(birthDate)
      validator.validField(birthDate)("birthDate")(dateRegex)

      validator.validStringField("address")(address)
    } catch {
      case e: FieldValidatorException => throw FieldValidatorException(String.format("%s %s", e.getClass, e.getMessage))
    }



  val age: Int = {
    val formatter: DateTimeFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd")
    println("calculating age inside class.")
    println(this.name)
    println(this.address)
    println(this.birthDate)
    val birthLocalDate: LocalDate = LocalDate.parse(this.birthDate, formatter)
    (Duration.between(birthLocalDate.atStartOfDay(), LocalDate.now().atStartOfDay()).toDays / 365).toInt
  }
}
