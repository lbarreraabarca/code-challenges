package com.data.factory.models

import org.scalatest._

class TestPerson extends FlatSpec {
  "test" should "my first test" in {
    val name = "name"
    val birthDate = "2000-01-01"
    val address = "My personal address # 145"
    val person: Person = new Person(name, birthDate, address)
    println("test person.age")
    assert(person.isValid)
    val expected: Int = 20
    assert(person.age > expected)
  }
}
